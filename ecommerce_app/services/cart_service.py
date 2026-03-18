from ecommerce_app.data import get_product


class CartError(Exception):
    pass


def get_session_cart(session):
    return session.setdefault("cart", {})


def add_to_cart(session, sku, quantity):
    product = get_product(sku)
    if product is None:
        raise CartError("Product not found")

    if quantity <= 0:
        raise CartError("Quantity must be greater than zero")

    cart = get_session_cart(session)
    current_qty = int(cart.get(sku, 0))
    new_qty = current_qty + quantity

    if new_qty > product.stock:
        raise CartError(f"Only {product.stock} units available for {product.name}")

    cart[sku] = new_qty
    session.modified = True


def remove_from_cart(session, sku):
    cart = get_session_cart(session)
    if sku in cart:
        del cart[sku]
        session.modified = True


def clear_cart(session):
    session["cart"] = {}
    session.modified = True


def cart_items(session):
    items = []
    cart = get_session_cart(session)

    for sku, qty in cart.items():
        product = get_product(sku)
        if product is None:
            continue

        quantity = int(qty)
        items.append(
            {
                "sku": product.sku,
                "name": product.name,
                "price": product.price,
                "quantity": quantity,
                "line_total": round(product.price * quantity, 2),
            }
        )

    return items


def cart_subtotal(session):
    return round(sum(item["line_total"] for item in cart_items(session)), 2)
