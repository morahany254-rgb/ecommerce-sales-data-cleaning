# 🛒 E-Commerce Sales Data Cleaning & Processing Pipeline

A robust Python-based data cleaning and preprocessing pipeline built using **Pandas** to transform messy, raw e-commerce transaction data into a clean, structured, and analysis-ready dataset.

---

## 📋 Project Overview
Real-world data is rarely clean. This project simulates a typical data engineering/analysis task where raw, unstructured e-commerce sales records contain missing values, inconsistent text formats, malformed dates, and corrupted numeric fields. The pipeline automates the extraction, cleaning, transformation, and export processes.

---

## 🛠️ Tech Stack & Libraries
* **Python 3.x**
* **Pandas** (Data manipulation and cleaning)
* **Openpyxl** (Excel file handling)

---

## 🧹 Key Cleaning Steps Implemented
1. **Handling Missing & Invalid IDs:** Dropped rows missing critical `Order ID` values and ensured correct numeric formatting.
2. **Text Standardization:** Cleaned and standardized categorical text columns (`Customer Name`, `Category`, `Payment Method`, `City`) using `.strip()` and `.title()` methods.
3. **Numeric Cleaning & Type Casting:**
   * Cleaned `Quantity` by mapping text-based numbers (e.g., `"two"`) and filtering out zero/negative values.
   * Cleaned `Unit Price` by stripping currency symbols (`$`, `EGP`) and comma separators.
   * Cleaned `Discount` percentages and converted them into proper float values.
4. **Feature Engineering:** Created a new calculated column **`Total price`** using the formula:
   $$\text{Total Price} = \text{Quantity} \times \text{Unit Price} \times (1 - \text{Discount})$$
5. **Date Parsing:** Standardized and converted `Order Date` into standard datetime objects.
6. **Column Reordering & Export:** Reordered columns logically and exported the cleaned dataset to a fresh Excel file.

---

## 📂 Project Structure
```text
├── ecommerce_messy_data.xlsx      # Raw, uncleaned dataset containing errors
├── Data cleaning.py               # Python script containing the cleaning pipeline
├── ecommerce_cleaned_data.xlsx    # Final cleaned and processed dataset
└── README.md                      # Project documentation
