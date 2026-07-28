# Stock Visualization Tool

<img width="886" height="495" alt="Screenshot 2026-07-28 at 15 03 55" src="https://github.com/user-attachments/assets/0f5118d8-4ab0-42ff-9b61-7618f914acaa" />

🔗 **[Try it live here](https://stockpriceanalyzerkymuella.streamlit.app/)**

## Background

A simple Stock Visualization Tool deployed through Streamlit. This project utilizes the yfinance API & displays a graph within an inputted time frame as well as various metrics such as average closing price, market volatility, etc. The purpose of this program is to allow the user to visualize a stock with any given time frame.

## Features
- Fetch historical stock data for any ticker & date range
- Interactive line chart of closing price
- Average, highest and lowest closing price
- Daily returns & market volatility
- Rolling averages & returns across multiple timeframes

## How to run locally
1. Clone this repo
2. Install dependencies: `pip install -r requirements.txt`
3. Run: `streamlit run app.py`

## What I learned
- Deploying a Webapp through Streamlit
- Data visualization through Streamlit
- Working with multi-index columns when pulling data from yfinance