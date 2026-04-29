# Low-Level Design (LLD)

1. Module-Level Design

1.1 Retrieval Module  
- Responsible for fetching relevant information from the knowledge base  
- Input: user query  
- Output: matched context  
- Uses keyword-based matching  

1.2 Small Talk Module  
- Handles greeting and casual queries  
- Prevents unnecessary escalation  
- Examples: hello, hi, how are you  

1.3 Intent Detection Module  
- Classifies queries into:
  - FAQ  
  - Escalation  
  - Unknown  

1.4 Confidence Module  
- Assigns confidence score  
- Context found → 0.9  
- No context → 0.2  

1.5 Processing Module  
- Combines query, context, intent, confidence  
- Decides next step  

1.6 Routing Module  
- Routes query to:
  - Response generation  
  - Escalation  

1.7 HITL Module  
- Handles escalation  
- Triggered when:
  - No data  
  - Low confidence  
  - User requests human  

1.8 Output Module  
- Returns final answer  
- Includes status  

---

2. Data Structures  

2.1 Graph State  
{
  "query": "string",
  "context": "string",
  "answer": "string",
  "escalate": "boolean"
}

2.2 Knowledge Base  
{
  "refund": "...",
  "warranty": "...",
  "shipping": "..."
}

2.3 Query-Response Schema  
{
  "query": "string",
  "answer": "string",
  "status": "resolved/escalated"
}

---

3. Workflow Design (LangGraph)  

Nodes:
- retrieve_context  
- process_query  
- generate_output  

Edges:
retrieve → process → output  

State Flow:
- Input → query  
- Retrieval → context  
- Processing → answer/escalate  
- Output → final answer  

---

4. Conditional Routing Logic  

Escalation triggered when:
- User asks for human  
- Confidence < 0.5  
- No context found  

Otherwise:
- System generates response  

---

5. HITL Design  

Trigger Conditions:
- Complex query  
- Unknown query  
- User request  

Flow:
1. System detects issue  
2. Marks escalation  
3. Returns response:
   "Escalated to human agent"  

---

6. API / Interface Design  

Input:
{
  "query": "What is refund policy?"
}

Output:
{
  "answer": "Refunds are allowed within 7 days",
  "status": "resolved"
}

---

7. Error Handling  

- Empty query → ask user again  
- No context → escalate  
- System failure → fallback message  

---

8. Execution Flow  

1. User enters query  
2. Query sent to system  
3. Retrieval module finds context  
4. Processing module evaluates  
5. Routing decision made  
6. Output returned  

---

9. Design Benefits  

- Modular design  
- Easy to extend  
- Clear workflow  
- Supports scaling  
- Better decision-making system  