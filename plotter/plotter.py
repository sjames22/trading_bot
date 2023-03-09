import matplotlib.pyplot as plt
import plotly.graph_objects as go
import yfinance as yf

data = yf.download("GC=F", start="2023-03-1", end="2023-03-9", interval='30M')


def plot():
    # plt.plot(dt.index, dt.Close)
    # plt.show()

    fig = go.Figure(data=go.Candlestick(
        x=data.index,
        open=data['Open'],
        high=data['High'],
        low=data['Low'],
        close=data['Close']))
    fig.update_layout(plot_bgcolor='black')
    fig.show()
