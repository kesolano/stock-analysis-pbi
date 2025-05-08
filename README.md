# 📈 NVIDIA Stock Analysis with Power BI and Python

This project analyzes the **percentage cumulative return** of NVIDIA's stock and includes a forecast for the next three years (**2025–2027**).

## 🔧 How to Use

1. **Run the Python script**
   - Execute `stock.py` to download and process historical stock data (NVIDIA) using Yahoo Finance.
   - The script generates an `Excel` file named `stock_data.xlsx`.

2. **Load the Excel file into Power BI**
   - Open `stock_data.xlsx` in Power BI.
   - Perform ETL steps (clean, transform) as needed.
   - Create visualizations such as:
     - Line charts of **Cumulative Return**
     - KPI cards for **Daily Return**, **Volatility**, and **Latest Return**
     - Forecasting charts using Power BI’s analytics tools

## 📊 Data Processed

- `Daily Return`
- `Cumulative Return`
- `30-Day Rolling Volatility`
- Ticker: **NVDA** (NVIDIA)

## 🧠 Requirements

- Python 3.x
- `pandas`, `yfinance`, `openpyxl`
- Power BI Desktop

## 📁 Files

- `stock.py`: Python script to fetch and process financial data
- `stock_data.xlsx`: Output data used in Power BI

---

**Disclaimer**: This analysis is for educational purposes only and does not constitute financial advice.
