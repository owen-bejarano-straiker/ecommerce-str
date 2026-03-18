TAX_RATE = 0.08
TIER_DISCOUNTS = {
    "regular": 0.00,
    "silver": 0.05,
    "gold": 0.10,
}
COUPON_DISCOUNTS = {
    "WELCOME10": 0.10,
    "SAVE20": 0.20,
}


def calculate_totals(subtotal, customer_tier="regular", coupon_code=None):
    tier_rate = TIER_DISCOUNTS.get(customer_tier.lower(), 0.0)
    coupon_rate = COUPON_DISCOUNTS.get((coupon_code or "").upper(), 0.0)
    discount = round(subtotal * (tier_rate + coupon_rate), 2)
    taxable_amount = subtotal - discount

    tax = round(taxable_amount * TAX_RATE, 2)
    total = round(taxable_amount + tax, 2)

    return {
        "subtotal": round(subtotal, 2),
        "discount": discount,
        "tax": tax,
        "total": total,
    }
