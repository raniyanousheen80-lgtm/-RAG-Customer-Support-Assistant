# Technical Documentation  
RAG-Based Customer Support Assistant (LangGraph + HITL)

--------------------------------------------------

1. Introduction  

1.1 What is RAG  
Retrieval-Augmented Generation (RAG) is an approach that combines information retrieval with response generation. Instead of generating answers purely from a language model, the system retrieves relevant data from a knowledge base and uses it to produce accurate and context-aware responses.

1.2 Why RAG is Needed  
Traditional chatbots often provide generic or incorrect responses due to lack of domain knowledge. RAG improves:
- Accuracy of responses  
- Context awareness  
- Reliability in customer support systems  

1.3 Use Case Overview  
This project implements a customer support assistant that:
- Answers FAQs (refund, warranty, shipping)  
- Handles user queries intelligently  
- Escalates complex queries to human agents  

--------------------------------------------------

2. System Architecture  

2.1 Architecture Overview  

User (Streamlit UI)  
        ↓  
Query Input  
        ↓  
LangGraph Workflow Engine  
        ↓  
Retrieval Layer (Knowledge Base)  
        ↓  
Processing Layer (Intent + Confidence)  
        ↓  
Decision / Routing Layer  
        ↓  
 ┌───────────────┬────────────────┐  
 │               │                │  
Response     Escalation      Small Talk  
 │               │                │  
Output Node   HITL Module    Direct Reply  
        ↓  
User Output  

--------------------------------------------------

2.2 Component Interaction  

- User enters query via web interface  
- Query is passed to LangGraph workflow  
- Retrieval node fetches relevant data  
- Processing node evaluates query  
- Routing logic decides action  
- Output node returns response  

--------------------------------------------------

3. Design Decisions  

3.1 Chunk Size  
Currently not implemented (simulated KB used), but ideal chunk size:
- 500 characters  
- Overlap: 100  

3.2 Embedding Strategy  
- Planned: vector embeddings using models  
- Current: keyword-based retrieval  

3.3 Retrieval Approach  
- Keyword matching for fast prototype  
- Can be replaced with similarity search  

3.4 Prompt Design Logic  
- Context + Query combined  
- Response generated based on retrieved data  

--------------------------------------------------

4. Workflow Explanation (LangGraph)  

4.1 Nodes  

- Retrieval Node → Fetch context  
- Processing Node → Apply logic  
- Output Node → Generate response  

4.2 State  

State object contains:
{
  "query": string,
  "context": string,
  "answer": string,
  "escalate": boolean
}

4.3 State Transitions  

Input → Retrieval → Processing → Output  

--------------------------------------------------

5. Conditional Logic  

5.1 Intent Detection  

Query classified into:
- FAQ  
- Escalation  
- Unknown  

5.2 Routing Decisions  

If:
- Context found → generate answer  
- No context → escalate  
- User requests human → escalate  

--------------------------------------------------

6. HITL (Human-in-the-Loop) Implementation  

6.1 Role of Human Intervention  

Used when:
- Query cannot be answered automatically  
- Confidence is low  
- User explicitly requests human  

6.2 Process  

1. System detects escalation condition  
2. Query flagged  
3. Response returned:
   "Escalated to human agent"  

6.3 Benefits  

- Improves reliability  
- Ensures customer satisfaction  
- Handles complex scenarios  

--------------------------------------------------

7. Challenges and Trade-offs  

7.1 Retrieval Accuracy vs Speed  
- Keyword search is fast but less accurate  
- Vector search is accurate but slower  

7.2 Chunk Size vs Context Quality  
- Large chunks → more context but slower  
- Small chunks → faster but less context  

7.3 Cost vs Performance  
- LLM APIs cost money  
- Simulated logic reduces cost  

--------------------------------------------------

8. Testing Strategy  

8.1 Testing Approach  

Manual testing with sample queries  

8.2 Sample Queries  

- "What is refund policy?"  
- "Tell me about warranty"  
- "I want to talk to human"  
- "hello"  

8.3 Expected Results  

- FAQ → correct answer  
- Unknown → escalation  
- Greeting → friendly response  

--------------------------------------------------

9. Future Enhancements  

- Add real PDF ingestion  
- Integrate ChromaDB (vector database)  
- Use real LLM (OpenAI / Gemini)  
- Add chat memory  
- Deploy on cloud  
- Improve UI design  

--------------------------------------------------

10. Conclusion  

This project demonstrates a RAG-based customer support system using LangGraph workflow and HITL escalation. The system is modular, scalable, and can be extended into a production-ready AI assistant.