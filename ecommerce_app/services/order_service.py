from ecommerce_app.services.pricing import calculate_totals


def validate_checkout_form(form):
    name = (form.get("name") or "").strip()
    tier = (form.get("tier") or "regular").strip().lower()
    coupon = (form.get("coupon") or "").strip().upper() or None

    if not name:
        return None, "Customer name is required"
    if tier not in {"regular", "silver", "gold"}:
        return None, "Customer tier must be regular, silver, or gold"

    return {"name": name, "tier": tier, "coupon": coupon}, None


def build_order(items, customer_name, tier, coupon):
    subtotal = round(sum(item["line_total"] for item in items), 2)
    totals = calculate_totals(subtotal, customer_tier=tier, coupon_code=coupon)

    return {
        "customer": customer_name,
        "tier": tier,
        "coupon": coupon,
        "items": items,
        "totals": totals,
    }
