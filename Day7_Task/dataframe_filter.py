# Task 4: Select Specific Columns and Filter Rows from a DataFrame

import pandas as pd

# --- Load CSV into a DataFrame ---
df = pd.read_csv(r"C:\Users\Ashok kumar\Desktop\Tasks\aiml-crash-Ashok_Kumar\Day7_Task\interns.csv")

#   Filter 1 — Active interns only 
active = df[df["status"] == "Active"][["name", "role", "score", "status"]]

print("\n" + "=" * 50)
print("  (Select specific columns)")
print("=" * 50)
print(active.to_string(index=False))

#  Filter 2 — Active interns scoring > 75 ─
# Condition: status == "Active" AND score > 75
top_active = df[
    (df["status"] == "Active") & (df["score"] > 75)
][["name", "role", "score", "department"]]

print("\n" + "=" * 50)
print("  (High performers who are currently Active AND score > 75)")
print("=" * 50)
print(top_active.to_string(index=False))
print(f"\n   {len(top_active)} intern(s) meet this criteria.\n")