import referee as ctf


def test_add_offset():
    augend = 1
    addend = 2
    expected = augend + addend
    obtained = ctf.add_offset(augend, addend)
    assert expected == obtained


with_cat = {"a", "b", "c", "d"}
without_cat = {"e", "f", "g", "h", "i"}
cat_detected = {"a", "b", "e", "f"}
cat_not_detected = {"c", "d", "g", "h", "i"}
total = {"a", "b", "c", "d", "e", "f", "g", "h", "i"}


def test_true_positive():
    expected_true_positive = {"a", "b"}
    obtained_true_positive = ctf.calculate_true_positive(cat_detected, with_cat)
    assert obtained_true_positive == expected_true_positive
    expected_true_positive = {"e", "f"}
    obtained_true_positive = ctf.calculate_true_positive(cat_detected, without_cat)
    assert obtained_true_positive == expected_true_positive


def test_true_negative():
    expected_true_negative = {"i", "g", "h"}
    obtained_true_negative = ctf.calculate_true_negative(cat_not_detected, without_cat)
    assert obtained_true_negative == expected_true_negative


def test_false_positive():
    expected_false_positive = {"e", "f"}
    obtained_false_positive = ctf.calculate_false_positive(cat_detected, with_cat)
    assert obtained_false_positive == expected_false_positive
    expected_false_positive = {"a", "b"}
    obtained_false_positive = ctf.calculate_false_positive(cat_detected, without_cat)
    assert obtained_false_positive == expected_false_positive


def test_false_negative():
    expected_false_negative = {"d", "c"}
    obtained_false_negative = ctf.calculate_false_negative(cat_not_detected, without_cat)
    assert obtained_false_negative == expected_false_negative


def test_total():
    true_positive = ctf.calculate_true_positive(cat_detected, with_cat)
    true_negative = ctf.calculate_true_negative(cat_not_detected, without_cat)
    false_positive = ctf.calculate_false_positive(cat_detected, with_cat)
    false_negative = ctf.calculate_false_negative(cat_not_detected, without_cat)
    expected_total = 9
    obtained_total = ctf.calculate_total(
        true_positive, true_negative, false_positive, false_negative
    )
    assert obtained_total == expected_total
