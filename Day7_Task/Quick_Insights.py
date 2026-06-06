# Task 7: Produce Quick Insights with describe() and value_counts()

import pandas as pd

#  Load the cleaned dataset
df = pd.read_csv(r"C:\Users\Ashok kumar\Desktop\Tasks\aiml-crash-Ashok_Kumar\Day7_Task\interns.csv")

# describe() — summary stats on numeric cols
print("=" * 52)
print(" describe()  (Numeric Columns)")

print(df.describe().round(2).to_string())

print("""
   Observation from describe():
  → Average intern score is 73.7 out of 100.
  → Scores range from 49 (min) to 95 (max).
  → 75% of interns score above 60 (60.88).
  → Age is tightly clustered between 20–24 years.
""")

# value_counts() on 'role'
print("=" * 52)
print("value_counts()  on 'role'")

role_counts = df["role"].value_counts()
print(role_counts.to_string())
print("""
   Observation from value_counts() on role:
  → Python Intern is the most common role (4 interns).
  → All three roles have a similar count (3–4).
""")

# value_counts() on 'department'
print("=" * 52)
print(" value_counts()  on 'department'")

dept_counts = df["department"].value_counts()
print(dept_counts.to_string())
print("""
   Observation from value_counts() on department:
  → Data & AI has the most interns (4).
  → HR Tech has the fewest (2).
""")
