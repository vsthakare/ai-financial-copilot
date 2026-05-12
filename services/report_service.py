from services.market_data_service import (
    get_stock_price,
    get_stock_history
)

from services.news_service import get_stock_news

from tools.technical_indicators import (
    calculate_indicators
)

from services.llm_service import summarize_news


def generate_financial_report(ticker: str):

    # Market data
    current_price = get_stock_price(ticker)

    history = get_stock_history(ticker)

    indicators = calculate_indicators(history)

    # News
    news = get_stock_news(ticker)

    # AI summary
    ai_summary = summarize_news(news)

    report = {
        "ticker": ticker.upper(),
        "current_price": current_price,
        "technical_analysis": indicators,
        "news": news,
        "ai_summary": ai_summary
    }

    return report