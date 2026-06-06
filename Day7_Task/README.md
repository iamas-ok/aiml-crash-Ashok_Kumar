# aiml-crash-Ashok_Kumar Day7 — Task

![Python](https://img.shields.io/badge/Python-3.13.5+-blue?logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Library-Pandas-blue?logo=pandas&logoColor=white)
![NumPy](https://img.shields.io/badge/Library-NumPy-013243?logo=numpy&logoColor=white)

---

## Repository Structure

```
aiml-crash-Ashok_Kumar/
├── Day1_Task/
├── Day4_Task/
└── Day7_Task/
    ├── student_profile_card.py
    ├── json_report.py
    ├── learner_class.py
    ├── dataframe_filter.py
    ├── .loc_vs_iloc.py
    ├── fill_missing.py
    ├── Quick_Insights.py
    ├── numpy_arrays_slicing.py
    ├── numpy_mask_broadcast_similarity.py
    ├── interns.csv
    └── learner_data.json
```

---

## Day 7 — Practice Task (9 Tasks)

| # | File | Description | Run |
|---|------|-------------|-----|
| [Task1](./student_profile_card.py) | `student_profile_card.py` | Learner profile card using variables, dictionary, type-hinted function, and f-strings | `python student_profile_card.py` |
| [Task2](./json_report.py) | `json_report.py` | Reads a JSON file and prints a formatted report using f-strings and list comprehensions | `python json_report.py` |
| [Task3](./learner_class.py) | `learner_class.py` | Learner class with `__init__`, `get_profile()`, and `get_badge()` methods returning formatted strings | `python learner_class.py` |
| [Task4](./dataframe_filter.py) | `dataframe_filter.py` | Loads interns.csv into Pandas, selects specific columns, and filters rows with boolean conditions | `python dataframe_filter.py` |
| [Task5](./.loc_vs_iloc.py) | `.loc_vs_iloc.py` | Side-by-side demonstration of label-based `.loc` and position-based `.iloc` with row and column selection | `python .loc_vs_iloc.py` |
| [Task6](./fill_missing.py) | `fill_missing.py` | Inspects missing values with `isnull().sum()`, drops critical nulls with `dropna()`, fills others with `fillna()` | `python fill_missing.py` |
| [Task7](./Quick_Insights.py) | `Quick_Insights.py` | Runs `describe()` on numeric columns and `value_counts()` on categorical columns with observations | `python Quick_Insights.py` |
| [Task8](./numpy_arrays_slicing.py) | `numpy_arrays_slicing.py` | Creates NumPy arrays with four methods, prints shape/dtype/ndim, and demonstrates indexing and slicing | `python numpy_arrays_slicing.py` |
| [Task9](./numpy_mask_broadcast_similarity.py) | `numpy_mask_broadcast_similarity.py` | Boolean masking, broadcasted operations, normalization, and cosine similarity on vector pairs | `python numpy_mask_broadcast_similarity.py` |

### Data Files

| File | Description |
|------|-------------|
| [interns.csv](./interns.csv) | Sample intern dataset used by Tasks 4, 5, 6, and 7 |
| [learner_data.json](./learner_data.json) | JSON profile file with name, role, skills, and score used by Task 2 |

---

## Setup & Installation

```bash
# 1. Clone the repo
git clone https://github.com/your-username/aiml-crash-Ashok_Kumar.git
cd aiml-crash-Ashok_Kumar/Day7_Task

# 2. Create and activate virtual environment
python -m venv .venv
source .venv/bin/activate        # macOS / Linux
.venv\Scripts\activate           # Windows

# 3. Install dependencies
pip install pandas numpy
```

---

## Quick Reference — Key Concepts Covered

| Concept | Where Used | Description |
|---------|------------|-------------|
| `f-strings` | [Task1](./student_profile_card.py), [Task2](./json_report.py), [Task3](./learner_class.py) | Embed expressions directly inside strings using `f"..."` syntax for clean, readable output |
| Type Hints | [Task1](./student_profile_card.py), [Task3](./learner_class.py) | Annotates function parameters and return types — e.g. `def fn(x: dict) -> str` |
| Dictionary | [Task1](./student_profile_card.py) | Key-value store used to hold a learner profile; accessed with `profile["key"]` |
| `json.load()` | [Task2](./json_report.py) | Reads a `.json` file and parses it into a Python dictionary |
| List Comprehension | [Task2](./json_report.py) | Compact one-line syntax to transform or filter lists — e.g. `[x.upper() for x in skills]` |
| `class` & `__init__` | [Task3](./learner_class.py) | Blueprint for creating objects; `__init__` sets instance attributes on each new object |
| Instance Methods | [Task3](./learner_class.py) | Functions inside a class that operate on `self` — e.g. `get_profile()`, `get_badge()` |
| `pd.read_csv()` | [Task4](./dataframe_filter.py), [Task5](./.loc_vs_iloc.py), [Task6](./fill_missing.py), [Task7](./Quick_Insights.py) | Loads a CSV file into a Pandas DataFrame for analysis |
| Column Selection | [Task4](./dataframe_filter.py) | `df[["col1","col2"]]` picks specific columns from a DataFrame |
| Boolean Filtering | [Task4](./dataframe_filter.py) | `df[df["col"] > value]` returns rows that match a condition |
| Combined Conditions | [Task4](./dataframe_filter.py) | `df[(cond1) & (cond2)]` chains multiple filters with `&` (AND) or `\|` (OR) |
| `.loc` | [Task5](./.loc_vs_iloc.py) | Label-based row and column selection — both ends of a slice are **inclusive** |
| `.iloc` | [Task5](./.loc_vs_iloc.py) | Integer position-based selection — right end of a slice is **exclusive** |
| `isnull().sum()` | [Task6](./fill_missing.py) | Counts missing (`NaN`) values per column to identify where cleaning is needed |
| `dropna()` | [Task6](./fill_missing.py) | Removes rows that contain null values in specified critical columns |
| `fillna()` | [Task6](./fill_missing.py) | Replaces missing values with a mean, median, or default string — preserves row count |
| `describe()` | [Task7](./Quick_Insights.py) | Returns count, mean, std, min, quartiles, and max for all numeric columns at once |
| `value_counts()` | [Task7](./Quick_Insights.py) | Counts occurrences of each unique value in a categorical column — great for quick distribution view |
| `np.array()` | [Task8](./numpy_arrays_slicing.py) | Creates a NumPy array from a Python list |
| `np.arange()` | [Task8](./numpy_arrays_slicing.py) | Generates an array with evenly spaced values given start, stop, and step |
| `np.zeros()` | [Task8](./numpy_arrays_slicing.py) | Creates an array (or matrix) filled with zeros — useful as a placeholder |
| `np.linspace()` | [Task8](./numpy_arrays_slicing.py) | Generates N evenly spaced values between a start and end — inclusive on both ends |
| `shape`, `dtype`, `ndim` | [Task8](./numpy_arrays_slicing.py) | Array attributes: dimensions tuple, data type, and number of axes respectively |
| Negative Indexing | [Task8](./numpy_arrays_slicing.py) | `a[-1]` accesses the last element; `a[-3]` is third from the end |
| Array Slicing | [Task8](./numpy_arrays_slicing.py) | `a[1:5]` returns index 1–4; `a[::2]` every 2nd; `a[::-1]` reverses the array |
| 2D Slicing | [Task8](./numpy_arrays_slicing.py) | `a[1:4, 1:4]` extracts a submatrix; `a[:, -1]` selects the entire last column |
| Boolean Masking | [Task9](./numpy_mask_broadcast_similarity.py) | `arr[arr > 75]` filters array values without any `for` loop — vectorized and fast |
| Broadcasting | [Task9](./numpy_mask_broadcast_similarity.py) | Applying `arr * 1.1` or `arr + 5` scales every element automatically — no loop needed |
| Normalization | [Task9](./numpy_mask_broadcast_similarity.py) | `(x - min) / (max - min)` rescales all values to a 0–1 range |
| `np.dot()` | [Task9](./numpy_mask_broadcast_similarity.py) | Computes the dot product of two vectors — core operation in cosine similarity |
| `np.linalg.norm()` | [Task9](./numpy_mask_broadcast_similarity.py) | Calculates the magnitude (length) of a vector — used as the denominator in cosine similarity |
| Cosine Similarity | [Task9](./numpy_mask_broadcast_similarity.py) | Measures how similar two vectors are in direction; output ranges from -1 (opposite) to 1 (identical) |
| `if __name__ == "__main__"` | All Tasks | Ensures demo code only runs when the file is executed directly, not when imported as a module |

---