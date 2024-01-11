import referee as ctf

with_cat = {"a", "b", "c", "d"}
without_cat = {"e", "f", "g", "h", "i"}
cat_detected = {"a", "b", "e", "f"}
cat_not_detected = {"c", "d", "g", "h", "i"}
total = {"a", "b", "c", "d", "e", "f", "g", "h", "i"}


def test_true_positive():
    expected_true_positive = {"a", "b"}
    all_data = {"cat_detected": cat_detected, "with_cat": with_cat}
    obtained_true_positive = ctf.calculate_true_positive(all_data)
    assert obtained_true_positive == expected_true_positive
    expected_true_positive = {"e", "f"}
    all_data = {"cat_detected": cat_detected, "with_cat": without_cat}
    obtained_true_positive = ctf.calculate_true_positive(all_data)
    assert obtained_true_positive == expected_true_positive


def test_true_negative():
    expected_true_negative = {"i", "g", "h"}
    all_data = {"cat_not_detected": cat_not_detected, "without_cat": without_cat}
    obtained_true_negative = ctf.calculate_true_negative(all_data)
    assert obtained_true_negative == expected_true_negative


def test_false_positive():
    expected_false_positive = {"e", "f"}
    all_data = {"cat_detected": cat_detected, "with_cat": with_cat}
    obtained_false_positive = ctf.calculate_false_positive(all_data)
    assert obtained_false_positive == expected_false_positive
    expected_false_positive = {"a", "b"}
    all_data = {"cat_detected": cat_detected, "with_cat": without_cat}
    obtained_false_positive = ctf.calculate_false_positive(all_data)
    assert obtained_false_positive == expected_false_positive


def test_false_negative():
    expected_false_negative = {"d", "c"}
    all_data = {"cat_not_detected": cat_not_detected, "without_cat": without_cat}
    obtained_false_negative = ctf.xxcalculate_false_negative(all_data)
    assert obtained_false_negative == expected_false_negative


def test_total():
    all_data = {"cat_detected": cat_detected, "with_cat": with_cat}
    true_positive = ctf.calculate_true_positive(all_data)
    all_data = {"cat_not_detected": cat_not_detected, "without_cat": without_cat}
    true_negative = ctf.calculate_true_negative(all_data)
    all_data = {"cat_detected": cat_detected, "with_cat": with_cat}
    false_positive = ctf.calculate_false_positive(all_data)
    all_data = {"cat_not_detected": cat_not_detected, "without_cat": without_cat}
    false_negative = ctf.xxcalculate_false_negative(all_data)
    expected_total = 9
    obtained_total = ctf.calculate_total(
        true_positive, true_negative, false_positive, false_negative
    )
    assert obtained_total == expected_total
