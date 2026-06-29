#  E-Commerce Sales Performance Analysis

## Overview

This project presents an end-to-end **Exploratory Data Analysis (EDA)** of the **Brazilian E-Commerce Public Dataset by Olist**. It explores sales performance, customer behavior, product trends, seller contributions, payment preferences, customer satisfaction, and retention patterns — translating raw transactional data into clear, actionable business insights.

---

## Business Objective

To uncover patterns and trends in e-commerce sales data and deliver recommendations that support data-driven decisions in marketing, inventory planning, seller management, and customer retention.

---

## Dataset Description

The analysis combines multiple related Olist datasets:

| Table | Key Columns | Description |
|---|---|---|
| **Customers** | `customer_id`, `customer_unique_id`, `customer_city`, `customer_state` | Customer identity and location |
| **Orders** | `order_id`, `customer_id`, `order_purchase_timestamp` | Order status and timing |
| **Order Items** | `order_id`, `product_id`, `seller_id`, `price`, `freight_value` | Product-level transaction details |
| **Products** | `product_id`, `product_category_name_english` | Product information and category |
| **Sellers** | `seller_id` | Seller identity |
| **Payments** | `order_id`, `payment_type`, `payment_value` | Payment method and value |
| **Reviews** | `order_id`, `review_score` | Customer feedback and ratings |
| **Geolocation** | `customer_city`, `customer_state` | Regional/geographic data |
| **Category Translation** | `product_category_name_english` | English category names |

---

##  Data Cleaning

* Checked and handled missing values across all datasets
* Identified and removed duplicate records
* Converted date columns to proper `datetime` format
* Validated relationships and keys between tables
* Performed merge integrity checks
* Produced a single, clean, merged dataset ready for analysis

---

## Business Questions Addressed

1. Which product categories generate the highest revenue?
2. Which cities or regions contribute the most sales?
3. Which customer segments provide the highest business value?
4. What purchasing patterns exist in customer buying behavior?
5. Which products drive the most sales volume and revenue?
6. How do payment methods influence purchasing trends?
7. Which sellers contribute the most value?
8. How do review scores vary across product categories?
9. How does sales volume change across time periods?
10. Which customers/orders are repeat vs. one-time?
11. What data quality issues exist in the merged dataset?
12. How reliable is the merge across multiple source files?

---

## Analysis Performed

**Revenue Analysis**
- Revenue by product category
- Revenue contribution by individual products

**Geographic Analysis**
- Sales distribution by city
- Sales distribution by state

**Customer Analysis**
- Customer segmentation
- Repeat vs. one-time customer behavior
- Purchasing pattern trends

**Seller Analysis**
- Revenue contribution by seller

**Payment Analysis**
- Trends across payment methods

**Review Analysis**
- Review score patterns by category

**Time-Series Analysis**
- Monthly sales volume trends

**Data Quality Analysis**
- Missing values, duplicates, data type checks, and merge integrity

---

##  Key Findings

-  Revenue is concentrated in a small number of product categories.
-  A handful of cities and states account for the majority of sales.
-  Purchasing behavior follows identifiable seasonal and time-based patterns.
-  A small group of sellers generate a disproportionate share of revenue.
-  Credit card is the dominant payment method.
-  Customer satisfaction varies notably across categories.
-  Most customers are one-time buyers — a major retention opportunity.

---

##  Visualizations

- Top Product Categories by Revenue
- Sales by City and State
- Customer Segment Analysis
- Purchasing Pattern Trends
- Top Products by Revenue
- Revenue by Payment Method
- Top Sellers by Revenue
- Review Score Analysis
- Monthly Sales Trends
- Repeat vs. One-Time Customer Analysis

---

##  Technologies Used

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-11557C?style=for-the-badge&logo=python&logoColor=white)
![Seaborn](https://img.shields.io/badge/Seaborn-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Jupyter Notebook](https://img.shields.io/badge/Jupyter-F37626?style=for-the-badge&logo=jupyter&logoColor=white)

---

##  Project Structure


```text
aiml-crash-Ashok_Kumar/
├── Day1_Task/
├── Day4_task/
├── Day7_Task/
├── Day9_Task/
├── Mini_Project_1/
│   ├── Analysis_Report.docx
│   ├── Datasets.zip
├   |── DataSets
|   |── E-Comm_Sales_Analysis.ipynb
│   └── README.md
├── .gitignore
└── README.md
```

---
## Setup & Installation

```bash
# 1. Clone the repo
git clone https://github.com/your-username/aiml-crash-Ashok_Kumar.git
cd aiml-crash-Ashok_Kumar/Mini_Project_1

# 2. Create and activate virtual environment
python -m venv .venv
source .venv/bin/activate        # macOS / Linux
.venv\Scripts\activate           # Windows

# 3. Install dependencies
pip install numpy pandas matplotlib seaborn
```
---

##  Conclusion

Business performance is heavily influenced by a small set of products, categories, sellers, and geographic regions. Recognizing these concentration patterns enables smarter decisions in inventory management, marketing strategy, customer retention, and seller partnerships.

###  Recommendations

- Double down on top-performing product categories.
- Concentrate marketing spend in high-revenue regions.
- Strengthen relationships with top-performing sellers.
- Address quality/service issues in low-rated categories.
- Launch customer retention and loyalty programs to convert one-time buyers.
- Use historical sales trends to guide inventory planning and forecasting.
- Continuously track customer feedback to improve satisfaction.

---

