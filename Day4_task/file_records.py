# Task 03: File I/O — Student Records
# Creates students.csv, reads it back, calculates averages/grades, and writes results.csv.

import csv


def get_grade(avg: float) -> str:
    if avg >= 90: return 'A'
    elif avg >= 75: return 'B'
    elif avg >= 60: return 'C'
    elif avg >= 45: return 'D'
    else: return 'F'



students_data = [
    ["name",    "math", "science", "english"],
    ["Aarav",   92,     88,        95],
    ["Priya",   74,     68,        80],
    ["Rohan",   40,     55,        38],
    ["Sneha",   85,     90,        78],
    ["Karan",   60,     72,        65],
]

with open("students.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(students_data)

print("students.csv created.")


# Read students.csv and calculate averages 
results = []

with open("students.csv", "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        avg = (float(row["math"]) + float(row["science"]) + float(row["english"])) / 3
        results.append({
            "name":    row["name"],
            "average": round(avg, 2),
            "grade":   get_grade(avg)
        })

print("\nCalculated Results:")
for r in results:
    print(f"  {r['name']:<10} | Avg: {r['average']} | Grade: {r['grade']}")

# EXPLORE
# Write results.csv using DictWriter 
with open("results.csv", "w", newline="") as f:
    fieldnames = ["name", "average", "grade"]
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()       # DictWriter writes the header row automatically
    writer.writerows(results)

print("\nresults.csv written.")


# csv.writer vs csv.DictWriter
# csv.writer  → writes rows as plain lists; you manage column order yourself.
# csv.DictWriter → writes rows as dicts using named fieldnames; safer and more readable
#                  because column names are explicit — harder to mix up the order.