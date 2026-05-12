import sys
import os

sys.path.append(
    os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            ".."
        )
    )
)

import streamlit as st
import requests
import pandas as pd

from tools.chart_tools import create_stock_chart

API_BASE = API_BASE = "https://ai-financial-copilot-api.onrender.com"

# =====================================================
# PAGE CONFIG
# =====================================================

st.set_page_config(
    page_title="AI Financial Copilot",
    layout="wide"
)

st.title("📈 AI Financial Copilot")


# =====================================================
# SESSION STATE
# =====================================================

if "messages" not in st.session_state:
    st.session_state.messages = []

if "thread_id" not in st.session_state:
    st.session_state.thread_id = "vedant"


# =====================================================
# DISPLAY CHAT HISTORY
# =====================================================

for message in st.session_state.messages:

    with st.chat_message(message["role"]):

        st.markdown(message["content"])


# =====================================================
# USER INPUT
# =====================================================

user_prompt = st.chat_input(
    "Ask about stocks..."
)


# =====================================================
# HANDLE USER INPUT
# =====================================================

if user_prompt:

    # ================================================
    # SAVE USER MESSAGE
    # ================================================

    st.session_state.messages.append({
        "role": "user",
        "content": user_prompt
    })

    # ================================================
    # DISPLAY USER MESSAGE
    # ================================================

    with st.chat_message("user"):

        st.markdown(user_prompt)

    # ================================================
    # CALL BACKEND CHAT API
    # ================================================

    response = requests.post(
        f"{API_BASE}/chat",
        json={
            "query": user_prompt,
            "thread_id": st.session_state.thread_id
        }
    )

    data = response.json()

    results = data["responses"]

    # ================================================
    # DISPLAY ASSISTANT RESPONSE
    # ================================================

    with st.chat_message("assistant"):

        for result in results:

            ticker = result["ticker"]

            stock_price = result["stock_price"]

            technicals = result["technical_analysis"]

            ai_summary = result["ai_summary"]

            news = result["news"]

            # =========================================
            # FETCH HISTORY FOR CHART
            # =========================================

            history_response = requests.get(
                f"{API_BASE}/history/{ticker}"
            )

            history_data = history_response.json()

            history = history_data["history"]

            fig = create_stock_chart(
                history,
                ticker
            )

            # =========================================
            # DISPLAY ANALYSIS
            # =========================================

            st.divider()

            st.subheader(f"{ticker} Analysis")

            st.metric(
                "Current Price",
                f"${stock_price:.2f}"
            )

            st.plotly_chart(
                fig,
                use_container_width=True
            )

            # =========================================
            # TECHNICAL INDICATORS
            # =========================================

            st.subheader(
                "Technical Indicators"
            )

            col1, col2, col3 = st.columns(3)

            col1.metric(
                "RSI",
                f"{technicals['rsi']:.2f}"
            )

            col2.metric(
                "SMA 20",
                f"{technicals['sma_20']:.2f}"
            )

            col3.metric(
                "SMA 50",
                f"{technicals['sma_50']:.2f}"
            )

            # =========================================
            # AI SUMMARY
            # =========================================

            st.subheader(
                "AI Financial Summary"
            )

            st.markdown(ai_summary)

            # =========================================
            # NEWS
            # =========================================

            st.subheader("Latest News")

            for article in news:

                st.markdown(
                    f"• [{article['title']}]({article['url']})"
                )

        # =============================================
        # SAVE ASSISTANT MESSAGE
        # =============================================

        assistant_response = (
            "Financial analysis completed."
        )

        st.session_state.messages.append({
            "role": "assistant",
            "content": assistant_response
        })