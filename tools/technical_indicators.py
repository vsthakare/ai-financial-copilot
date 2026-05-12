import pandas as pd

from ta.trend import SMAIndicator
from ta.momentum import RSIIndicator


def calculate_indicators(history):

    df = pd.DataFrame(history)

    # Moving averages
    df["sma_20"] = SMAIndicator(
        close=df["close"],
        window=20
    ).sma_indicator()

    df["sma_50"] = SMAIndicator(
        close=df["close"],
        window=50
    ).sma_indicator()

    # RSI
    df["rsi"] = RSIIndicator(
        close=df["close"],
        window=14
    ).rsi()

    latest = df.iloc[-1]

    return {
        "sma_20": float(latest["sma_20"]),
        "sma_50": float(latest["sma_50"]),
        "rsi": float(latest["rsi"])
    }