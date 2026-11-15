from order import apply_tax, average_item_price, calculate_total


def test_total_no_discount():
    assert calculate_total([(10.0, 2)]) == 20.0


def test_total_with_discount():
    assert calculate_total([(100.0, 1)], 10) == 90.0


def test_average_item_price():
    assert average_item_price([(10.0, 2), (20.0, 1)]) == 15.0


def test_apply_tax():
    assert apply_tax(100.0, 20) == 120.0
