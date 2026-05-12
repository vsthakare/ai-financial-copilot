from typing import TypedDict, List, Dict, Any

from langgraph.graph import StateGraph, END
from langgraph.checkpoint.memory import MemorySaver

from services.market_data_service import (
    get_stock_price,
    get_stock_history
)

from services.news_service import get_stock_news

from services.llm_service import summarize_news

from tools.technical_indicators import (
    calculate_indicators
)


# ======================================================
# SHARED STATE
# ======================================================

class FinancialState(TypedDict):

    ticker: str

    user_query: str

    conversation_history: list

    stock_price: float

    technical_analysis: Dict[str, Any]

    news: List[Dict[str, Any]]

    ai_summary: str


# ======================================================
# AGENT NODES
# ======================================================

def market_agent(state: FinancialState):

    ticker = state["ticker"]

    stock_price = get_stock_price(ticker)

    return {
        **state,
        "stock_price": stock_price
    }


def technical_agent(state: FinancialState):

    ticker = state["ticker"]

    history = get_stock_history(ticker)

    indicators = calculate_indicators(history)

    return {
        **state,
        "technical_analysis": indicators
    }


def news_agent(state: FinancialState):

    ticker = state["ticker"]

    news = get_stock_news(ticker)

    return {
        **state,
        "news": news
    }


def report_agent(state: FinancialState):

    summary = summarize_news(state["news"])

    return {
        **state,
        "ai_summary": summary
    }


# ======================================================
# LANGGRAPH WORKFLOW
# ======================================================

workflow = StateGraph(FinancialState)

workflow.add_node(
    "market_agent",
    market_agent
)

workflow.add_node(
    "technical_agent",
    technical_agent
)

workflow.add_node(
    "news_agent",
    news_agent
)

workflow.add_node(
    "report_agent",
    report_agent
)


# ======================================================
# WORKFLOW EDGES
# ======================================================

workflow.set_entry_point("market_agent")

workflow.add_edge(
    "market_agent",
    "technical_agent"
)

workflow.add_edge(
    "technical_agent",
    "news_agent"
)

workflow.add_edge(
    "news_agent",
    "report_agent"
)

workflow.add_edge(
    "report_agent",
    END
)


# ======================================================
# MEMORY
# ======================================================

memory = MemorySaver()


# ======================================================
# COMPILE GRAPH
# ======================================================

financial_graph = workflow.compile(
    checkpointer=memory
)


# ======================================================
# EXECUTION FUNCTION
# ======================================================

def run_financial_workflow(
    ticker: str,
    thread_id: str = "default"
):

    initial_state = {
    "ticker": ticker,
    "user_query": f"Analyze {ticker}",
    "conversation_history": []
}

    result = financial_graph.invoke(
        initial_state,
        config={
            "configurable": {
                "thread_id": thread_id
            }
        }
    )

    return result