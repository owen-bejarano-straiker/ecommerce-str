from ecommerce_app.models import Product

PRODUCTS = {
    "KB001": Product("KB001", "Mechanical Keyboard", "Peripherals", 79.99, 35),
    "MS001": Product("MS001", "Wireless Mouse", "Peripherals", 32.50, 60),
    "MN001": Product("MN001", "27in Monitor", "Displays", 249.00, 18),
    "HD001": Product("HD001", "Headphones", "Audio", 119.00, 25),
    "DK001": Product("DK001", "USB-C Dock", "Accessories", 89.00, 22),
    "ST001": Product("ST001", "Laptop Stand", "Accessories", 34.90, 50),
}


def list_products():
    return list(PRODUCTS.values())


def get_product(sku):
    return PRODUCTS.get(sku)
