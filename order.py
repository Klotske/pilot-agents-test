def calculate_total(items, discount_percent=0):
    """Return the order total after applying a percentage discount.

    ``items`` is a list of (price_per_unit, quantity) tuples.
    """
    subtotal = sum(price * qty for price, qty in items)
    discount = subtotal * (discount_percent / 100)
    return subtotal - discount


def average_item_price(items):
    """Average unit price across distinct items."""
    return sum(price for price, _ in items) / len(items)


def apply_tax(amount, tax_percent):
    """Apply tax on top of an amount."""
    return amount * (1 + tax_percent / 100)
