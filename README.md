# AI Financial Copilot

An AI-powered financial analysis platform built using **FastAPI, LangGraph, Streamlit, and LLM APIs** for conversational stock analysis, technical indicators, market news summarization, and multi-company comparison.

---

# Features

## Conversational Financial AI
- Chat-based stock analysis
- Multi-company comparison
- Context-aware conversations
- Thread-based conversational memory

---

## Real-Time Market Data
- Live stock prices
- Historical stock data
- Candlestick charts
- Moving averages

---

## Technical Analysis
- RSI
- SMA 20
- SMA 50
- Quantitative market insights

---

## AI-Powered Insights
- Financial news summarization
- Market sentiment analysis
- AI-generated investment reports
- Risk analysis

---

## Agentic AI Workflow
Built using **LangGraph** with multiple agents:
- Market Agent
- Technical Analysis Agent
- News Agent
- Report Generation Agent

---

## Interactive Frontend
- ChatGPT-style UI using Streamlit
- Interactive charts using Plotly
- Financial dashboards
- Comparison analysis

---

# Tech Stack

## Backend
- FastAPI
- Python
- LangGraph
- LangChain

## Frontend
- Streamlit
- Plotly

## AI / LLM
- Groq API
- Llama 3.3 70B
- Conversational AI workflows

## Financial Data
- Yahoo Finance API (`yfinance`)
- NewsAPI

---

# Project Architecture

```text
User Prompt
    ↓
Chat Endpoint
    ↓
LangGraph Workflow
    ↓
┌─────────────────────┐
│ Market Agent        │
│ Technical Agent     │
│ News Agent          │
│ Report Agent        │
└─────────────────────┘
    ↓
LLM Financial Summary
    ↓
Streamlit Frontend
```

---

# Folder Structure

```text
financial-agent/
│
├── app/
│   ├── __init__.py
│   └── main.py
│
├── frontend/
│   └── streamlit_app.py
│
├── services/
│   ├── __init__.py
│   ├── llm_service.py
│   ├── market_data_service.py
│   ├── news_service.py
│   └── report_service.py
│
├── tools/
│   ├── __init__.py
│   ├── chart_tools.py
│   └── technical_indicators.py
│
├── workflows/
│   └── financial_workflow.py
│
├── utils/
│   ├── __init__.py
│   └── parser.py
│
├── .env.example
├── requirements.txt
└── README.md
```

---

# Setup Instructions

## 1️⃣ Clone Repository

```bash
git clone https://github.com/vsthakare/ai-financial-copilot
cd financial-agent
```

---

## 2️⃣ Create Virtual Environment

### Mac/Linux

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### Windows

```bash
python -m venv .venv
.venv\Scripts\activate
```

---

## 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Environment Variables

Create a `.env` file:

```env
NEWS_API_KEY=your_newsapi_key
GROQ_API_KEY=your_groq_api_key
```

---

# ▶️ Run Backend

```bash
uvicorn app.main:app --reload --port 8001
```

Swagger Docs:

```text
http://127.0.0.1:8001/docs
```

---

# ▶️ Run Frontend

```bash
streamlit run frontend/streamlit_app.py
```

Frontend:

```text
http://localhost:8501
```

---

# Live Demo

Frontend: https://ai-financial-copilot-airpr7cfewbene9rtqzkex.streamlit.app/p

Backend API Docs: https://ai-financial-copilot-api.onrender.com/

---

# Example Prompts

```text
Analyze NVDA stock
```

```text
Compare NVDA and AMD
```

```text
Analyze Tesla stock
```

```text
Compare Apple and Microsoft
```

---


# Future Improvements

- Vector database memory
- RAG over SEC filings
- Portfolio optimization
- Autonomous trading simulation
- Voice-enabled financial assistant
- Real-time websocket streaming
- Advanced multi-agent routing

---

# Key Learnings

This project demonstrates:
- Agentic AI architecture
- LangGraph orchestration
- Backend engineering
- LLM integration
- Conversational AI
- Financial analytics
- API integration
- Stateful workflows
- Multi-agent systems

---

# Author

Vedant Thakare

---

# License

MIT License

