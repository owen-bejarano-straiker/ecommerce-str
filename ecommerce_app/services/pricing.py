TAX_RATE = 0.08


def calculate_totals(subtotal):
    tax = round(subtotal * TAX_RATE, 2)
    total = round(subtotal + tax, 2)

    return {
        "subtotal": round(subtotal, 2),
        "discount": 0.0,
        "tax": tax,
        "total": total,
    }
