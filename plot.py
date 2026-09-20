# /// script
# requires-python = ">=3.10"
# dependencies = ["matplotlib"]
# ///

import csv
import matplotlib.pyplot as plt
DATA_FILE = "data/daily_HKO_RF_2026.csv"
MONTH = 2

days = []
rainfall = []

with open(DATA_FILE, encoding="utf-8-sig") as file:
    reader = csv.reader(file)

    # Skip the first two description lines
    next(reader)
    next(reader)
    next(reader)  # header

    for row in reader:
        if len(row) < 4:
            continue

        month = int(row[1])

        if month == MONTH:
            days.append(int(row[2]))
            value = 0.0 if row[3] == "Trace" else float(row[3])
            rainfall.append(value)

plt.bar(days, rainfall)

plt.xlabel("Day")
plt.ylabel("Rainfall (mm)")
plt.title("Hong Kong Daily Rainfall — February 2026")

plt.savefig("out/rainfall.png")
plt.show()