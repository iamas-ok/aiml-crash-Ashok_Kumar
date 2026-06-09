# aiml-crash-Ashok_Kumar Day9 — Task

![Python](https://img.shields.io/badge/Python-3.13.5+-blue?logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Library-Pandas-blue?logo=pandas&logoColor=white)
![SQLite](https://img.shields.io/badge/Database-SQLite-003B57?logo=sqlite&logoColor=white)

---

## Repository Structure

```text
aiml-crash-Ashok_Kumar/
├── Day1_Task/
├── Day4_Task/
├── Day7_Task/
└── Day9_Task/
    ├── Pandas_Visualization_SQL.ipynb
    ├── customers.csv
    ├── products.csv
    ├── orders.csv
    └── sales.db
```

---

## Day 9 — Practice Assignment (9 Tasks)

| # | Task | Description |
|---|------|-------------|
| Task1 | Dataset Audit | Load dataset and perform audit (shape, columns, dtypes, nulls, duplicates, unique counts) |
| Task2 | Data Cleaning | Standardize columns, fix datatypes, handle missing values, remove duplicates |
| Task3 | GroupBy Analysis | Analyze sales by region, category, and customer segment using groupby |
| Task4 | KPI Analysis | Merge tables and calculate revenue, profit, AOV, top-selling products |
| Task5 | Pivot Tables | Create pivot tables for region vs month and category vs segment |
| Task6 | Visualizations | Create histogram, scatter plot, bar chart, line chart, box plot, and heatmap |
| Task7 | Business Insights | Write business story and insights from charts |
| Task8 | SQLite & SQL | Create SQLite database and execute SQL queries |
| Task9 | Pandas vs SQL | Compare the same analysis using Pandas and SQL |

### Data Files

| File | Description |
|------|-------------|
| customers.csv | Customer dataset containing region and segment information |
| products.csv | Product dataset containing category, price, and cost |
| orders.csv | Order transaction dataset |
| sales.db | SQLite database created from the datasets |

---

## Setup & Installation

```bash
# 1. Clone the repo
git clone https://github.com/your-username/aiml-crash-Ashok_Kumar.git
cd aiml-crash-Ashok_Kumar/Day9_Task

# 2. Create and activate virtual environment
python -m venv .venv
source .venv/bin/activate        # macOS / Linux
.venv\Scripts\activate           # Windows

# 3. Install dependencies
pip install pandas matplotlib seaborn
```

---

## Quick Reference — Key Concepts Covered

| Concept | Where Used | Description |
|---------|------------|-------------|
| `pd.read_csv()` | Task1, Task2 | Load CSV files into DataFrames |
| Data Audit | Task1 | Analyze shape, columns, datatypes, nulls, duplicates, unique counts |
| `isnull().sum()` | Task1, Task2 | Detect missing values |
| `duplicated()` | Task1, Task2 | Detect duplicate rows |
| `fillna()` | Task2 | Handle missing values |
| `drop_duplicates()` | Task2 | Remove duplicate records |
| `pd.to_datetime()` | Task2 | Convert columns to datetime datatype |
| `groupby()` | Task3 | Aggregate data by region, category, and segment |
| Multi-Level GroupBy | Task3 | Analyze data across multiple dimensions |
| `merge()` | Task4 | Combine customers, products, and orders tables |
| KPI Analysis | Task4 | Revenue, Profit, AOV, Top Products |
| `pivot_table()` | Task5 | Create multidimensional summaries |
| Histogram | Task6 | Revenue distribution analysis |
| Scatter Plot | Task6 | Quantity vs Revenue relationship |
| Bar Chart | Task6 | Category-wise revenue comparison |
| Line Chart | Task6 | Monthly revenue trend |
| Box Plot | Task6 | Revenue distribution by region |
| Heatmap | Task6 | Region vs Month performance comparison |
| Business Insights | Task7 | Interpret charts and identify trends |
| `sqlite3` | Task8 | Create SQLite database |
| SQL Queries | Task8 | SELECT, WHERE, GROUP BY, ORDER BY, JOIN, HAVING |
| Aggregate Functions | Task8 | COUNT, SUM, AVG |
| Subqueries | Task8 | Advanced SQL analysis |
| Pandas vs SQL | Task9 | Compare analysis using both tools |

---
