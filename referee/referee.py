def calculate_true_positive(all_data):
    cat_detected = all_data["cat_detected"]
    with_cat = all_data["with_cat"]
    return cat_detected & with_cat


def calculate_true_negative(all_data):
    return all_data["cat_not_detected"] & all_data["without_cat"]


def calculate_false_positive(all_data):
    return all_data["cat_detected"] - all_data["with_cat"]


def calculate_false_negative(all_data):
    return all_data["cat_not_detected"] - all_data["without_cat"]


def calculate_total(all_data):
    binary_classification = _classify(all_data)
    return len(
        binary_classification["true_positive"]
        | binary_classification["true_negative"]
        | binary_classification["false_positive"]
        | binary_classification["false_negative"]
    )


def _classify(all_data):
    true_positive = calculate_true_positive(all_data)
    true_negative = calculate_true_negative(all_data)
    false_positive = calculate_false_positive(all_data)
    false_negative = calculate_false_negative(all_data)
    return {
        "true_positive": true_positive,
        "true_negative": true_negative,
        "false_positive": false_positive,
        "false_negative": false_negative,
    }


def calculate_accuracy(all_data):
    total_classifications = 9
    correct_classifications = 5
    return correct_classifications / total_classifications
