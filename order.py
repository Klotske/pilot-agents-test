def calculate_total(items, discount_percent=0):
    """Return the order total after applying a percentage discount.

    ``items`` is a list of (price_per_unit, quantity) tuples.
    """
    subtotal = sum(price * qty for price, qty in items)
    return subtotal * (1 - discount_percent / 100)
