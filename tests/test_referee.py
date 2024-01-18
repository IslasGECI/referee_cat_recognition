import geci_referee as ctf

with_cat = {"a", "b", "c", "d"}
without_cat = {"e", "f", "g", "h", "i"}
cat_detected = {"a", "b", "e", "f"}
cat_not_detected = {"c", "d", "g", "h", "i"}
all = {"a", "b", "c", "d", "e", "f", "g", "h", "i"}

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


def test_accuracy():
    all_classifications = 9
    correct_classifications = 5
    expected_accuracy = correct_classifications / all_classifications
    obtained_accuracy = ctf.calculate_accuracy(all_data)
    assert obtained_accuracy == expected_accuracy


def test_sensibility():
    expected_sensibility = 0.5
    obtained_sensibility = ctf.calculate_sensibility(all_data)
    assert obtained_sensibility == expected_sensibility


def test_specificity():
    expected_specificity = 0.6
    obtained_specificity = ctf.calculate_specificity(all_data)
    assert obtained_specificity == expected_specificity


def test_average_true_rate():
    expected_average_true_rate = 0.55
    obtained_average_true_rate = ctf.calculate_balanced_accuracy(all_data)
    assert obtained_average_true_rate == expected_average_true_rate
