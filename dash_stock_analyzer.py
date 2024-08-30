import dash
import dash_bootstrap_components as dbc
from dash import dcc, html
from dash.dependencies import Input, Output
import yfinance as yf
import plotly.graph_objs as go
import pandas as pd

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = dbc.Container([
    dbc.Row([
        dbc.Col(html.H1("Stock Market Analyzer", className="text-center mb-4"), width=12)
    ]),
    dbc.Row([
        dbc.Col([
            dcc.Input(id="ticker-input", type="text", value="AAPL", className="mb-2"),
            dcc.DatePickerRange(
                id="date-picker-range",
                start_date=pd.to_datetime("2020-01-01"),
                end_date=pd.to_datetime("2024-01-01"),
                display_format='YYYY-MM-DD'
            ),
            dcc.Checklist(
                id="indicator-checklist",
                options=[
                    {"label": "SMA", "value": "SMA"},
                    {"label": "EMA", "value": "EMA"},
                    {"label": "Bollinger Bands", "value": "BB"},
                    {"label": "RSI", "value": "RSI"},
                ],
                value=["SMA", "EMA"],
                inline=True
            ),
            dbc.Button("Update", id="update-button", color="primary", className="mt-2"),
        ], width=4),
        dbc.Col(dcc.Graph(id="stock-graph"), width=8)
    ])
], fluid=True)

@app.callback(
    Output("stock-graph", "figure"),
    [
        Input("ticker-input", "value"),
        Input("date-picker-range", "start_date"),
        Input("date-picker-range", "end_date"),
        Input("indicator-checklist", "value")
    ]
)
def update_graph(ticker, start_date, end_date, selected_indicators):
    stock_data = yf.download(ticker, start=start_date, end=end_date)
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=stock_data.index, y=stock_data['Close'], mode='lines', name='Close Price'))

    if "SMA" in selected_indicators:
        stock_data['SMA_20'] = stock_data['Close'].rolling(window=20).mean()
        fig.add_trace(go.Scatter(x=stock_data.index, y=stock_data['SMA_20'], mode='lines', name='SMA 20'))

    if "EMA" in selected_indicators:
        stock_data['EMA_20'] = stock_data['Close'].ewm(span=20, adjust=False).mean()
        fig.add_trace(go.Scatter(x=stock_data.index, y=stock_data['EMA_20'], mode='lines', name='EMA 20'))

    if "BB" in selected_indicators:
        stock_data['BB_Middle'] = stock_data['Close'].rolling(window=20).mean()
        stock_data['BB_Upper'] = stock_data['BB_Middle'] + 2 * stock_data['Close'].rolling(window=20).std()
        stock_data['BB_Lower'] = stock_data['BB_Middle'] - 2 * stock_data['Close'].rolling(window=20).std()
        fig.add_trace(go.Scatter(x=stock_data.index, y=stock_data['BB_Upper'], mode='lines', name='BB Upper'))
        fig.add_trace(go.Scatter(x=stock_data.index, y=stock_data['BB_Lower'], mode='lines', name='BB Lower'))

    if "RSI" in selected_indicators:
        delta = stock_data['Close'].diff(1)
        gain = delta.where(delta > 0, 0)
        loss = -delta.where(delta < 0, 0)
        avg_gain = gain.rolling(window=14).mean()
        avg_loss = loss.rolling(window=14).mean()
        rs = avg_gain / avg_loss
        rsi = 100 - (100 / (1 + rs))
        fig.add_trace(go.Scatter(x=stock_data.index, y=rsi, mode='lines', name='RSI'))

    fig.update_layout(title=f"{ticker} Stock Price and Indicators", xaxis_title='Date', yaxis_title='Price', template='plotly_dark')
    return fig

if __name__ == "__main__":
    app.run_server(debug=True)
