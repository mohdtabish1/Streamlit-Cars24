import streamlit as st
import yfinance as yf
import datetime as dt

st.write("Stock price Analyzer")
st.subheader("This application helps you to analyze the stock price of a company")

col1, col2, col3 = st.columns(3)

# ticker = yf.Ticker("MSFT")  # APPL GOOG TSLA AMZN
with col1:
    symbol = st.text_input("Enter the stock symbol", value="MSFT")
ticker = yf.Ticker(symbol)
# ticker_data = ticker.history(period="1mo")

with col2:
    start_date = st.date_input("Start date", dt.date.today() - dt.timedelta(days=30))

with col3:
    end_date = st.date_input("End date", dt.date.today())

ticker_data = ticker.history(start=start_date, end=end_date)

st.write(ticker_data)

st.subheader("Price Movement")

st.line_chart(ticker_data["Close"])

st.header("Volume Movement")
st.bar_chart(ticker_data["Volume"])
