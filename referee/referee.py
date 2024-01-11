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


def calculate_total(true_positive, true_negative, false_positive, false_negative):
    all_data = {
        "true_positive": true_positive,
        "true_negative": true_negative,
        "false_positive": false_positive,
        "false_negative": false_negative,
    }
    return xxcalculate_total(all_data)


def xxcalculate_total(all_data):
    return len(
        all_data["true_positive"]
        | all_data["true_negative"]
        | all_data["false_positive"]
        | all_data["false_negative"]
    )
