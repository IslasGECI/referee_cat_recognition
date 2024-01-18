import pandas as pd
import os
import geci_referee as ctf

hidden_data = pd.read_csv("/workdir/data/all_photos.csv")
with_cat = set(hidden_data[hidden_data["presence"] == 1]["filename"])
without_cat = set(hidden_data[hidden_data["presence"] == 0]["filename"])
cat_detected = set(os.listdir("/workdir/cat_detected"))
cat_not_detected = (with_cat | without_cat) - cat_detected

all_data = {
    "cat_detected": cat_detected,
    "cat_not_detected": cat_not_detected,
    "with_cat": with_cat,
    "without_cat": without_cat,
}
accuracy = ctf.calculate_accuracy(all_data)
print(f"Accuracy: {round(accuracy*100)}%")
sensitivity = ctf.calculate_sensitivity(all_data)
print(f"Sensitivity: {round(sensitivity*100)}%")
specificity = ctf.calculate_specificity(all_data)
print(f"Specificity: {round(specificity*100)}%")
balanced_accuracy = ctf.calculate_balanced_accuracy(all_data)
print(f"Balanced accuracy: {round(balanced_accuracy*100)}%")

