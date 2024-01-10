def calculate_true_positive(all_data):
    cat_detected = all_data["cat_detected"]
    with_cat = all_data["with_cat"]
    return cat_detected & with_cat


def calculate_true_negative(all_data):
    return all_data["cat_not_detected"] & all_data["without_cat"]


def calculate_false_positive(cat_detected, with_cat):
    return xxcalculate_false_positive(cat_detected, with_cat)


def xxcalculate_false_positive(cat_detected, with_cat):
    return cat_detected - with_cat


def calculate_false_negative(cat_not_detected, without_cat):
    return cat_not_detected - without_cat


def calculate_total(true_positive, true_negative, false_positive, false_negative):
    return len(true_positive | true_negative | false_positive | false_negative)
