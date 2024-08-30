import streamlit as st
import yfinance as yf
import pandas as pd
import plotly.graph_objs as go

# Set up the Streamlit app
st.set_page_config(page_title="Stock Market Analyzer", layout="wide")

st.title("📈 Stock Market Analyzer")

# Sidebar for user input
st.sidebar.header("User Input")
ticker = st.sidebar.text_input("Enter Stock Ticker", "AAPL").upper()
start_date = st.sidebar.date_input("Start Date", pd.to_datetime("2020-01-01"))
end_date = st.sidebar.date_input("End Date", pd.to_datetime("2024-01-01"))
selected_indicators = st.sidebar.multiselect(
    "Select Technical Indicators",
    ["Simple Moving Average (SMA)", "Exponential Moving Average (EMA)", "Bollinger Bands", "Relative Strength Index (RSI)"]
)

# Fetch data from yfinance
try:
    stock_data = yf.download(ticker, start=start_date, end=end_date)
except Exception as e:
    st.error(f"Error fetching data: {e}")
    st.stop()

# Display raw data
st.subheader(f"Raw Data for {ticker}")
st.write(stock_data.tail())

# Plotting the stock price
st.subheader(f"{ticker} Closing Price")
fig = go.Figure()
fig.add_trace(go.Scatter(x=stock_data.index, y=stock_data['Close'], mode='lines', name='Close Price'))

# Add indicators to the plot
if "Simple Moving Average (SMA)" in selected_indicators:
    stock_data['SMA_20'] = stock_data['Close'].rolling(window=20).mean()
    fig.add_trace(go.Scatter(x=stock_data.index, y=stock_data['SMA_20'], mode='lines', name='SMA 20'))

if "Exponential Moving Average (EMA)" in selected_indicators:
    stock_data['EMA_20'] = stock_data['Close'].ewm(span=20, adjust=False).mean()
    fig.add_trace(go.Scatter(x=stock_data.index, y=stock_data['EMA_20'], mode='lines', name='EMA 20'))

if "Bollinger Bands" in selected_indicators:
    stock_data['BB_Middle'] = stock_data['Close'].rolling(window=20).mean()
    stock_data['BB_Upper'] = stock_data['BB_Middle'] + 2 * stock_data['Close'].rolling(window=20).std()
    stock_data['BB_Lower'] = stock_data['BB_Middle'] - 2 * stock_data['Close'].rolling(window=20).std()
    fig.add_trace(go.Scatter(x=stock_data.index, y=stock_data['BB_Upper'], mode='lines', name='BB Upper'))
    fig.add_trace(go.Scatter(x=stock_data.index, y=stock_data['BB_Lower'], mode='lines', name='BB Lower'))

if "Relative Strength Index (RSI)" in selected_indicators:
    delta = stock_data['Close'].diff(1)
    gain = delta.where(delta > 0, 0)
    loss = -delta.where(delta < 0, 0)
    avg_gain = gain.rolling(window=14).mean()
    avg_loss = loss.rolling(window=14).mean()
    rs = avg_gain / avg_loss
    rsi = 100 - (100 / (1 + rs))
    fig.add_trace(go.Scatter(x=stock_data.index, y=rsi, mode='lines', name='RSI'))

fig.update_layout(title=f"{ticker} Stock Price and Indicators", xaxis_title='Date', yaxis_title='Price', template='plotly_dark')
st.plotly_chart(fig, use_container_width=True)
