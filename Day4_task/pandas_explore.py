# Task 07: Pandas — Explore a Dataset
# Creates a student DataFrame and answers analytical questions using Pandas.

import pandas as pd

#  Create DataFrame of 10 students 
data = {
    "name":          ["Aarav", "Priya", "Rohan", "Sneha", "Karan",
                      "Meera", "Arjun", "Divya", "Rahul", "Pooja"],
    "city":          ["Jaipur", "Delhi", "Mumbai", "Jaipur", "Delhi",
                      "Mumbai", "Jaipur", "Delhi", "Mumbai", "Jaipur"],
    "math_score":    [92, 74, 40, 85, 60, 78, 88, 55, 70, 95],
    "science_score": [88, 68, 55, 90, 72, 82, 76, 60, 65, 91],
    "english_score": [95, 80, 38, 78, 65, 74, 83, 70, 58, 89],
}

df = pd.DataFrame(data)
df["total"] = df["math_score"] + df["science_score"] + df["english_score"]

print(" Full Dataset ")
print(df.to_string(index=False))

#  Average score in each subject 
print("\nAverage score per subject ")
print(df[["math_score", "science_score", "english_score"]].mean())

#  Student with the highest total score 
print("\nHighest total score ")
print(df.loc[df["total"].idxmax(), ["name", "total"]])

# Number of students from each city 
print("\nStudents per city ")
print(df.groupby("city")["name"].count())

# Students with math score above 75 
print("\nStudents with math score > 75 ")
print(df[df["math_score"] > 75][["name", "city", "math_score"]].to_string(index=False))

#  EXPLORE: Top 3 students by total score using nlargest 
print("\n Explore: Top 3 students by total score ")
print(df.nlargest(3, "total")[["name", "total"]].to_string(index=False))

# nlargest(n, column) returns the n rows with the largest values in the given column.
# It is cleaner and more readable than sort_values().tail(3) for finding top-N rows.