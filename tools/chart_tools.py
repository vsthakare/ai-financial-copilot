import pandas as pd
import plotly.graph_objects as go


def create_stock_chart(history, ticker):

    df = pd.DataFrame(history)

    df["sma_20"] = df["close"].rolling(20).mean()
    df["sma_50"] = df["close"].rolling(50).mean()

    fig = go.Figure()

    # Candlestick chart
    fig.add_trace(
        go.Candlestick(
            x=df["date"],
            open=df["open"],
            high=df["high"],
            low=df["low"],
            close=df["close"],
            name="Price"
        )
    )

    # SMA 20
    fig.add_trace(
        go.Scatter(
            x=df["date"],
            y=df["sma_20"],
            mode="lines",
            name="SMA 20"
        )
    )

    # SMA 50
    fig.add_trace(
        go.Scatter(
            x=df["date"],
            y=df["sma_50"],
            mode="lines",
            name="SMA 50"
        )
    )

    fig.update_layout(
        title=f"{ticker} Stock Price",
        xaxis_title="Date",
        yaxis_title="Price",
        template="plotly_white"
    )

    return fig