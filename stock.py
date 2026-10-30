import streamlit as st
import yfinance as yf
import datetime as dt

st.write("Stock price Analyzer")
st.subheader("This application helps you to analyze the stock price of a company")

# ticker = yf.Ticker("MSFT")  # APPL GOOG TSLA AMZN
synbol = st.text_input("Enter the stock symbol", value="MSFT")
ticker = yf.Ticker(synbol)
ticker_data = ticker.history(period="1mo")
st.write(ticker_data)

st.subheader("Price Movement")

st.line_chart(ticker_data["Close"])

st.header("Volume Movement")
st.bar_chart(ticker_data["Volume"])
