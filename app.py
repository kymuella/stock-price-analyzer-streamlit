import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
import numpy as np


# functions

def closing(data,ticker):
    return data["Close", ticker]

def avgclosingprice(data,ticker):
    return data["Close", ticker].mean()

def highestclosingprice(data,ticker):
    return data["Close", ticker].max()

def lowestclosingprice(data,ticker):
    return data["Close", ticker].min()

    # calculate biggest single-day loss/gain & daily differences

def calculatedailydifferences(data,ticker):
    dailyDiff = data["Close",ticker].diff()
    dailyDiff.name = "Daily Returns" 
    dailyDiff = dailyDiff.fillna(0)
     
    return dailyDiff.min(), dailyDiff.max() # biggest single day loss, gain


    # calculate daily returns as a percentage
def calculatedailyreturns(data,ticker):
    return (data["Close",ticker] - data["Close",ticker].shift(1)) / data["Close",ticker].shift(1)

    # market volatility
def calculatevolatility(data,ticker):
    return ((data["Close",ticker] - data["Close",ticker].shift(1)) / data["Close",ticker].shift(1)).std()

    # rolling averages + total return over period
def onedayavgs(data,ticker):

    return (data["Close",ticker].rolling(window=1).mean()).fillna(0), (data["Close", ticker] / data["Close", ticker].shift(1) - 1).fillna(0)

def sevendayavgs(data,ticker):
    return (data["Close",ticker].rolling(window=5).mean()).fillna(0), (data["Close", ticker] / data["Close", ticker].shift(5) - 1).fillna(0)

def onemonthavgs(data,ticker):
    return (data["Close",ticker].rolling(window=21).mean()).fillna(0), (data["Close", ticker] / data["Close", ticker].shift(21) - 1).fillna(0)

def threemonthavgs(data,ticker):
    return (data["Close",ticker].rolling(window=63).mean()).fillna(0), (data["Close", ticker] / data["Close", ticker].shift(63) - 1).fillna(0)

def sixmonthavgs(data,ticker):
    return (data["Close",ticker].rolling(window=126).mean()).fillna(0), (data["Close", ticker] / data["Close", ticker].shift(126) - 1).fillna(0)

def yearlyavgs(data,ticker): 
    return (data["Close",ticker].rolling(window=252).mean()).fillna(0), (data["Close", ticker] / data["Close", ticker].shift(252) - 1).fillna(0)

def displaycalculations(data,ticker):
    st.write("Average Closing Price: " + str(round(avgclosingprice(data,ticker),4)))
    st.write("Highest Closing Price: " + str(round(highestclosingprice(data,ticker),4)))
    st.write("Lowest Closing Price: " + str(round(lowestclosingprice(data,ticker),4)))
    st.write("Market Volatility: " + str(round(calculatevolatility(data,ticker)*100,4)) + "%")

    options = st.selectbox(
        "Select Rolling Average",
        ["1 day", "7 days", "1 month", "3 months", "6 months", "1 year"],
)



    
    if "1 day" in options:   
        oda, odr = onedayavgs(data,ticker)
        st.write("One day Average: $" + str(round(oda.iloc[-1],4)))
        st.write("One day Return: " + str(round(odr.iloc[-1]*100,4)) + "%")
    if "7 days" in options:
        sda, sdr = sevendayavgs(data,ticker)
        st.write("Seven day Average: $" + str(round(sda.iloc[-1],4)))
        st.write("Seven day Return: " + str(round(sdr.iloc[-1]*100,4)) + "%")
    if "1 month" in options:
        oma, omr = onemonthavgs(data,ticker)
        st.write("One month Average: $" + str(round(oma.iloc[-1],4)))
        st.write("One month Return: " + str(round(omr.iloc[-1]*100,4)) + "%")
    if "3 months" in options:
        tma, tmr = threemonthavgs(data,ticker)
        st.write("Three month Average: $" + str(round(tma.iloc[-1],4)))            
        st.write("Three month Return: " + str(round(tmr.iloc[-1]*100,4)) + "%")        
    if "6 months" in options:
        sma, smr = sixmonthavgs(data,ticker)
        st.write("Six month Average: $" + str(round(sma.iloc[-1],4)))
        st.write("Six month Return: " + str(round(smr.iloc[-1]*100,4)) + "%")
    if "1 year" in options:
        ya, yr = yearlyavgs(data,ticker)
        st.write("Yearly Average: $" + str(round(ya.iloc[-1],4)))
        st.write("Yearly Return: " + str(round(yr.iloc[-1] * 100,4)) + "%") 

# StreamLit WebApp

st.set_page_config(layout="wide")
st.markdown("<h1 style='text-align: center;'>Stock Visualization Tool</h1>", unsafe_allow_html=True)

col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    ticker = st.text_input("Input a ticker:")
    start = st.date_input("Start date:")
    end = st.date_input("End date:")
    if st.button("Fetch Data", key="fetch_button"):
        st.session_state["data"] = yf.download(ticker, start=start, end=end)


if "data" in st.session_state:
    d = st.session_state["data"]
    st.write(d)
    close = closing(d, ticker)
    close.name = "Closing Price"
    st.line_chart(close, x_label="Date", y_label="Closing Price", height=500, width=2000)    
    displaycalculations(d, ticker)


    





