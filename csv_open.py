# Your script should output something similar to this (based on the provided CSV content):

# Contents of CSV:
# Name,Age,Score
# John,23,88
# Doe,34,92
# Jane,29,95
# Smith,40,78

# Average Score: 88.25
# Highest Scorer: Jane
# Average Age: 31.5

import os
import csv


def open_file():
    sum_score = 0
    ct = 0
    age_total = 0
    max_score = 0
    highest_scorer = ''
    print("Contents of CSV:")
    with open("example.csv") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            print(",".join(row.values()))
            score = int(row["Score"])
            sum_score += score
            age_total += int(row["Age"])
            ct += 1
            if score > max_score:
                max_score = score
                highest_scorer = row["Name"]

    print(f"Average Score: {sum_score/ct}")
    print(f"Highest Scorer: {highest_scorer}")
    print(f"Average Age: {age_total/ct}")


# Average Score: 88.25
# Highest Scorer: Jane
# Average Age: 31.5
print(open_file())
