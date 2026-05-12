def extract_tickers(query: str):

    query = query.upper()

    known_tickers = [
        "AAPL",
        "NVDA",
        "AMD",
        "TSLA",
        "MSFT",
        "GOOG"
    ]

    found = []

    for ticker in known_tickers:

        if ticker in query:
            found.append(ticker)

    if not found:
        found.append("AAPL")

    return found