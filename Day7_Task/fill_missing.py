# task6.py



import pandas as pd
import numpy as np

data = {
    "Name": ["Ashok", "Ravi", None, "Neha"],
    "Score": [85, np.nan, 90, 78]
}

df = pd.DataFrame(data)

print("Missing Values:")
print(df.isnull().sum())

print("\nUsing dropna():")
print(df.dropna())

df["Score"] = df["Score"].fillna(df["Score"].mean())

print("\nUsing fillna():")
print(df)