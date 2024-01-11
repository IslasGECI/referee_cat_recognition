import referee as ctf

with_cat = {"a", "b", "c", "d"}
without_cat = {"e", "f", "g", "h", "i"}
cat_detected = {"a", "b", "e", "f"}
cat_not_detected = {"c", "d", "g", "h", "i"}
total = {"a", "b", "c", "d", "e", "f", "g", "h", "i"}

all_data = {
    "cat_detected": cat_detected,
    "cat_not_detected": cat_not_detected,
    "with_cat": with_cat,
    "without_cat": without_cat,
}


def test_true_positive():
    expected_true_positive = {"a", "b"}
    obtained_true_positive = ctf.calculate_true_positive(all_data)
    assert obtained_true_positive == expected_true_positive


def test_true_negative():
    expected_true_negative = {"i", "g", "h"}
    obtained_true_negative = ctf.calculate_true_negative(all_data)
    assert obtained_true_negative == expected_true_negative


def test_false_positive():
    expected_false_positive = {"e", "f"}
    obtained_false_positive = ctf.calculate_false_positive(all_data)
    assert obtained_false_positive == expected_false_positive


def test_false_negative():
    expected_false_negative = {"d", "c"}
    obtained_false_negative = ctf.calculate_false_negative(all_data)
    assert obtained_false_negative == expected_false_negative


def test_total():
    expected_total = 9
    obtained_total = ctf.calculate_total(all_data)
    assert obtained_total == expected_total


def test_accuracy():
    total_classifications = 9
    correct_classifications = 5
    expected_accuracy = correct_classifications / total_classifications
    obtained_accuracy = ctf.calculate_accuracy(all_data)
    assert obtained_accuracy == expected_accuracy
