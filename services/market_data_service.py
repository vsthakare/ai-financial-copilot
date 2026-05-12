import yfinance as yf

def get_stock_price(ticker: str):
    stock = yf.Ticker(ticker)

    hist = stock.history(period="1d")

    if hist.empty:
        return None

    return float(hist["Close"].iloc[-1])

def get_stock_history(ticker: str, period: str = "6mo"):

    stock = yf.Ticker(ticker)

    hist = stock.history(period=period)

    if hist.empty:
        return None

    hist.reset_index(inplace=True)

    data = []

    for _, row in hist.iterrows():

        data.append({
            "date": str(row["Date"]),
            "open": float(row["Open"]),
            "high": float(row["High"]),
            "low": float(row["Low"]),
            "close": float(row["Close"]),
            "volume": int(row["Volume"])
        })

    return data