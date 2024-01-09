def add_offset(augend: int, addend: int) -> int:
    return augend + addend


def calculate_true_positive(cat_detected, with_cat):
    return cat_detected & with_cat


def xxcalculate_true_positive(cat_detected, with_cat):
    return calculate_true_positive(cat_detected, with_cat)


def calculate_true_negative(cat_not_detected, without_cat):
    return cat_not_detected & without_cat


def calculate_false_positive(cat_detected, with_cat):
    return cat_detected - with_cat


def calculate_false_negative(cat_not_detected, without_cat):
    return cat_not_detected - without_cat


def calculate_total(true_positive, true_negative, false_positive, false_negative):
    return len(true_positive | true_negative | false_positive | false_negative)
