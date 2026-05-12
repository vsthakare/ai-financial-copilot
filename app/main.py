from fastapi import FastAPI
from services.market_data_service import (
    get_stock_price,
    get_stock_history
)
from tools.technical_indicators import calculate_indicators
from services.news_service import get_stock_news
from services.llm_service import summarize_news
from services.report_service import (
    generate_financial_report
)
from workflows.financial_workflow import (
    run_financial_workflow
)
from pydantic import BaseModel
from utils.parser import extract_tickers

app = FastAPI()


class ChatRequest(BaseModel):

    query: str

    thread_id: str = "default"


@app.get("/")
def home():
    return {"message": "Financial Agent Running"}


@app.get("/price/{ticker}")
def price(ticker: str):

    stock_price = get_stock_price(ticker)

    if stock_price is None:
        return {"error": "Ticker not found"}

    return {
        "ticker": ticker.upper(),
        "price": stock_price
    }

@app.get("/history/{ticker}")
def history(ticker: str):

    data = get_stock_history(ticker)

    if data is None:
        return {"error": "Ticker not found"}

    return {
        "ticker": ticker.upper(),
        "history": data
    }

@app.get("/analysis/{ticker}")
def analyze(ticker: str):

    history = get_stock_history(ticker)

    if history is None:
        return {"error": "Ticker not found"}

    indicators = calculate_indicators(history)

    return {
        "ticker": ticker.upper(),
        "technical_analysis": indicators
    }

@app.get("/news/{ticker}")
def news(ticker: str):

    articles = get_stock_news(ticker)

    return {
        "ticker": ticker.upper(),
        "news": articles
    }

@app.get("/summary/{ticker}")
def summary(ticker: str):

    news = get_stock_news(ticker)

    result = summarize_news(news)

    return {
        "ticker": ticker.upper(),
        "summary": result
    }

@app.get("/report/{ticker}")
def report(ticker: str):

    result = generate_financial_report(ticker)

    return result

@app.get("/agent/{ticker}")
def run_agent(
    ticker: str,
    thread_id: str = "default"
):

    result = run_financial_workflow(
        ticker,
        thread_id
    )

    return result


@app.post("/chat")
def chat(request: ChatRequest):

    query = request.query

    thread_id = request.thread_id

    tickers = extract_tickers(query)

    results = []

    for ticker in tickers:

        result = run_financial_workflow(
            ticker=ticker,
            thread_id=thread_id
        )

        results.append(result)

    return {
        "query": query,
        "responses": results
    }