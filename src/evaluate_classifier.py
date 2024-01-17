import pandas as pd
import os

hidden_data = pd.read_csv("/workdir/data/all_photos.csv")
with_cat = set(hidden_data[hidden_data["presence"] == 1]["filename"])
without_cat = set(hidden_data[hidden_data["presence"] == 0]["filename"])

cat_detected = set(os.listdir("/workdir/cat_detected"))
print(cat_detected)
all_data = {
    "cat_detected": cat_detected,
    "cat_not_detected": cat_not_detected,
    "with_cat": with_cat,
    "without_cat": without_cat,
}
