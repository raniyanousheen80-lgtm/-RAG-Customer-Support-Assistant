# High-Level Design (HLD)

## 1. System Overview

### Problem Definition
Customer support systems often rely on static FAQs or manual responses, leading to delayed or inaccurate answers. Users expect quick, contextual, and intelligent responses.

### Proposed Solution
This project implements a Retrieval-Augmented Generation (RAG) based Customer Support Assistant that:
- Retrieves relevant information from a knowledge base
- Generates contextual responses
- Uses a graph-based workflow (LangGraph) for control logic
- Supports Human-in-the-Loop (HITL) escalation for complex queries

### Scope of System
- Process queries related to customer support (refund, warranty, shipping)
- Provide automated responses using retrieval
- Escalate to human when required
- Provide a web-based chat interface

---

## 2. Architecture Diagram (Textual Representation)

User (Web UI - Streamlit)
        ↓
Query Input
        ↓
LangGraph Workflow Engine
        ↓
[Retrieval Node] → Knowledge Base
        ↓
[Processing Node]
        ↓
Decision Layer (Routing)
        ↓
 ┌───────────────┬────────────────┐
 │               │                │
Response     Escalation     Small Talk
 │               │                │
Output Node   HITL Module    Direct Response
        ↓
User Response (UI)

---

## 3. Component Description

### 3.1 User Interface (Streamlit)
- Chat-based interface for user interaction
- Displays conversation history
- Sends user queries to backend

---

### 3.2 Document Loader (Conceptual)
- Loads knowledge base (simulated in this project)
- Can be extended to load PDFs

---

### 3.3 Chunking Strategy
- Splits large documents into smaller chunks (future enhancement)
- Improves retrieval accuracy

---

### 3.4 Embedding Model (Conceptual)
- Converts text into vector embeddings
- Not implemented (simulated retrieval used)

---

### 3.5 Vector Store (Future Integration)
- Stores embeddings for fast similarity search
- Example: ChromaDB

---

### 3.6 Retriever
- Matches user query with knowledge base
- Returns relevant context

---

### 3.7 LLM Layer (Simulated)
- Generates responses based on retrieved context
- Currently rule-based

---

### 3.8 Graph Workflow Engine (LangGraph)
- Core control system
- Defines nodes and edges
- Manages execution flow

Nodes:
- Retrieval Node
- Processing Node
- Output Node

---

### 3.9 Routing Layer
- Performs decision making based on:
  - Intent detection
  - Confidence score
- Routes query to:
  - Response generation
  - HITL escalation

---

### 3.10 HITL Module
- Handles escalation cases
- Triggered when:
  - No context found
  - User explicitly requests human
  - Low confidence

---

## 4. Data Flow

1. User enters query in UI
2. Query sent to LangGraph workflow
3. Retrieval node extracts relevant context
4. Processing node evaluates intent and confidence
5. Routing decision is made:
   - If valid → generate response
   - If invalid → escalate
6. Output node returns final response
7. UI displays result

---

## 5. Technology Choices

| Component | Technology | Reason |
|----------|--------|--------|
| UI | Streamlit | Simple web interface |
| Workflow | LangGraph | Structured execution |
| Language | Python | Flexibility |
| Storage | In-memory | Fast prototype |
| Future DB | ChromaDB | Vector search |

---

## 6. Scalability Considerations

- Replace in-memory KB with vector DB
- Add async query processing
- Support multi-document ingestion
- Deploy on cloud (AWS/GCP)
- Cache frequent queries

---

## 7. System Advantages

- Modular design
- Easy to extend
- Real-time decision making
- Supports escalation
- Clear workflow control