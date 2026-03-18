TAX_RATE = 0.08
COUPON_DISCOUNTS = {
    "WELCOME10": 0.10,
    "SAVE20": 0.20,
}


def calculate_totals(subtotal, coupon_code=None):
    print(f"[pricing] subtotal={subtotal:.2f}")

    rate = COUPON_DISCOUNTS.get((coupon_code or "").upper(), 0.0)
    discount = round(subtotal * rate, 2)
    taxable_amount = subtotal - discount

    tax = round(taxable_amount * TAX_RATE, 2)
    total = round(taxable_amount + tax, 2)

    print(f"[pricing] coupon_discount={discount:.2f}")
    print(f"[pricing] total={total:.2f}")

    return {
        "subtotal": round(subtotal, 2),
        "discount": discount,
        "tax": tax,
        "total": total,
    }
