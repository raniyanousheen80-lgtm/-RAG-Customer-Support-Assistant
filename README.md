# 🤖 RAG-Based Customer Support Assistant

### 🚀 LangGraph + HITL Powered AI System

## 📌 Overview

This project implements a **Retrieval-Augmented Generation (RAG)** based Customer Support Assistant designed to provide intelligent, context-aware responses.

The system leverages a **LangGraph workflow** for structured execution and includes **Human-in-the-Loop (HITL)** escalation to handle complex or ambiguous queries.


## 🎯 Key Features

* 🔍 **RAG-based Retrieval System**
* 🔄 **LangGraph Workflow Execution**
* 🧠 **Intent Detection & Confidence Scoring**
* 🔀 **Conditional Routing Logic**
* 👨‍💻 **Human-in-the-Loop (HITL) Escalation**
* 💬 **Interactive Chat UI (Streamlit)**


## 🏗️ System Architecture

```
User (Streamlit UI)
        ↓
Query Input
        ↓
LangGraph Workflow
        ↓
Retrieval Layer
        ↓
Processing Layer (Intent + Confidence)
        ↓
Routing Decision
   ┌───────────────┬────────────────┐
   │               │                │
Response     Escalation        Small Talk
   │               │                │
Output        HITL Module     Direct Reply
        ↓
User Output



## ⚙️ Tech Stack

| Component       | Technology         |
| --------------- | ------------------ |
| UI              | Streamlit          |
| Backend         | Python             |
| Workflow Engine | LangGraph          |
| Retrieval       | Simulated KB       |
| Future Scope    | ChromaDB, LLM APIs |

---

## 📂 Project Structure

```
RAG-Customer-Support-Assistant/
│
├── app.py
├── streamlit_app.py
├── requirements.txt
├── HLD.md
├── LLD.md
├── TECHNICAL_DOCUMENTATION.md
├── sample_kb.pdf
```

---

## ▶️ How to Run

### 1. Install dependencies

```
pip install -r requirements.txt
```

### 2. Run the app

```
streamlit run streamlit_app.py
```

---

## 🧠 How It Works

1. User enters a query
2. System retrieves relevant context
3. LangGraph processes query
4. Intent & confidence evaluated
5. Routing decision applied:

   * ✅ Generate response
   * ⚠️ Escalate to human
   * 💬 Handle small talk

---

## 🔁 HITL (Human-in-the-Loop)

Escalation is triggered when:

* No relevant context is found
* Confidence score is low
* User explicitly requests human support

---

## 🧪 Sample Queries

* `What is refund policy?`
* `Tell me about warranty`
* `I want to talk to human`
* `hello`

---

## 🚧 Future Enhancements

* 📄 PDF ingestion pipeline
* 🧠 Real embedding models
* 🗄️ ChromaDB integration
* 🤖 LLM integration (OpenAI / Gemini)
* ☁️ Cloud deployment
* 💾 Chat memory

---

## 📊 Evaluation Highlights

* ✔️ RAG Implementation
* ✔️ LangGraph Workflow
* ✔️ Conditional Routing
* ✔️ HITL Integration
* ✔️ Full Documentation (HLD, LLD, Technical)


This project is developed as part of an academic evaluation focusing on **AI system design, workflow orchestration, and applied RAG architecture**.
