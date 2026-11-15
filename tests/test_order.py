from order import calculate_total


def test_total_no_discount():
    assert calculate_total([(10.0, 2)]) == 20.0


def test_total_with_discount():
    assert calculate_total([(100.0, 1)], 10) == 90.0
