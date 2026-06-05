# Task 5: Compare .loc and .iloc on the Same Dataset

import pandas as pd

# Load dataset
df = pd.read_csv("C:\\Users\\Ashok kumar\\Desktop\\Tasks\\aiml-crash-Ashok_Kumar\\Day7_Task\\interns.csv")

# Set 'name' as index so .loc labels are meaningful
df.index = df["name"]
df = df.drop(columns=["name"])

# .loc  → Label-based: use actual row/column NAMES
print("  .loc  →  LABEL-BASED SELECTION")

#Single row by name, specific columns
loc_ex = df.loc["Sneha Patel", ["role", "score", "status"]]
print(f"Select Sneha Patel's row using her name as label")
print(loc_ex.to_string())

print("=" * 55)

# .iloc → Position-based: use integer row/col INDEX
print("  .iloc →  POSITION-BASED SELECTION")

#  Row 3, columns 0 and 1
iloc_ex = df.iloc[3, 0:2]
print(f"  (Row at position 3, columns at position 0 and 1)")
print(iloc_ex.to_string())

print("=" * 55)

print(" KEY DIFFERENCE-->")

print("""
  .loc  → Uses LABELS (names, column headers).
           Row slicing is INCLUSIVE on both ends.
           e.g. df.loc['Priya':'Karan'] includes Karan.

  .iloc → Uses INTEGER POSITIONS (0, 1, 2 ...).
           Row slicing is EXCLUSIVE on the right end.
           e.g. df.iloc[0:4] gives rows 0, 1, 2, 3 only.

  → Know the name?  Use .loc
  → Know the index? Use .iloc
""")