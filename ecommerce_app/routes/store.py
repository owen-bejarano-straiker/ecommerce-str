from flask import Blueprint, flash, redirect, render_template, request, session, url_for

from ecommerce_app.data import list_products
from ecommerce_app.services.cart_service import (
    CartError,
    add_to_cart,
    cart_items,
    cart_subtotal,
    clear_cart,
    remove_from_cart,
)
from ecommerce_app.services.order_service import build_order, validate_checkout_form

store_bp = Blueprint("store", __name__)


@store_bp.get("/")
def home():
    return render_template("index.html", products=list_products())


@store_bp.post("/cart/add")
def cart_add():
    sku = (request.form.get("sku") or "").strip()
    qty_raw = (request.form.get("quantity") or "1").strip()

    try:
        quantity = int(qty_raw)
        add_to_cart(session, sku, quantity)
        flash("Item added to cart", "success")
    except ValueError:
        flash("Quantity must be a number", "error")
    except CartError as exc:
        flash(str(exc), "error")

    return redirect(url_for("store.home"))


@store_bp.post("/cart/remove")
def cart_remove():
    sku = (request.form.get("sku") or "").strip()
    remove_from_cart(session, sku)
    flash("Item removed from cart", "success")
    return redirect(url_for("store.cart_view"))


@store_bp.get("/cart")
def cart_view():
    items = cart_items(session)
    subtotal = cart_subtotal(session)
    return render_template("cart.html", items=items, subtotal=subtotal)


@store_bp.get("/checkout")
def checkout_page():
    items = cart_items(session)
    if not items:
        flash("Your cart is empty", "error")
        return redirect(url_for("store.home"))

    subtotal = cart_subtotal(session)
    return render_template("checkout.html", items=items, subtotal=subtotal)


@store_bp.post("/checkout")
def checkout_submit():
    items = cart_items(session)
    if not items:
        flash("Your cart is empty", "error")
        return redirect(url_for("store.home"))

    checkout_data, error = validate_checkout_form(request.form)
    if error:
        flash(error, "error")
        return redirect(url_for("store.checkout_page"))

    order = build_order(
        items,
        customer_name=checkout_data["name"],
        tier=checkout_data["tier"],
        coupon=checkout_data["coupon"],
    )

    clear_cart(session)
    return render_template("order_confirmation.html", order=order)
