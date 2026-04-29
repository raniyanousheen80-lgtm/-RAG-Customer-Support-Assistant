from langgraph.graph import StateGraph
from typing import TypedDict

# ---------------- STATE -----------------


class GraphState(TypedDict):
    query: str
    context: str
    answer: str
    escalate: bool

# ---------------- KNOWLEDGE BASE ----------------
knowledge_base = {
    "refund": "Refunds are allowed within 7 days of purchase.",
    "warranty": "Products come with a 1-year warranty.",
    "shipping": "Shipping takes 3-5 business days."
}

# ---------------- RETRIEVAL ----------------
def retrieve_context(state: GraphState):
    query = state["query"]
    context = ""

    for key in knowledge_base:
        if key in query.lower():
            context = knowledge_base[key]

    return {"context": context}

# ---------------- SMALL TALK (FIX) ----------------
def handle_small_talk(query):
    q = query.lower()

    if "hello" in q or "hi" in q:
        return "Hello! How can I assist you today?"
    
    if "how are you" in q:
        return "I'm an AI assistant, here to help you!"
    
    if "thanks" in q:
        return "You're welcome! 😊"

    return None

# ---------------- INTENT ----------------
def detect_intent(query):
    q = query.lower()

    if "human" in q or "agent" in q:
        return "escalation"
    
    if any(word in q for word in ["refund", "warranty", "shipping"]):
        return "faq"
    
    return "unknown"

# ---------------- CONFIDENCE ----------------
def calculate_confidence(context):
    if context == "":
        return 0.2
    return 0.9

# ---------------- PROCESS NODE ----------------
def process_query(state: GraphState):
    query = state["query"]

    # ✅ FIRST: handle greetings
    small = handle_small_talk(query)
    if small:
        return {
            "answer": small,
            "escalate": False
        }

    context = state.get("context", "")

    intent = detect_intent(query)
    confidence = calculate_confidence(context)

    # Escalation conditions
    if intent == "escalation" or confidence < 0.5:
        return {"escalate": True}

    return {
        "answer": context,
        "escalate": False
    }

# ---------------- OUTPUT ----------------
def generate_output(state: GraphState):
    if state.get("escalate"):
        return {"answer": "⚠️ Escalated to human agent."}

    return {"answer": state.get("answer", "No answer found.")}

# ---------------- GRAPH ----------------
builder = StateGraph(GraphState)

builder.add_node("retrieve", retrieve_context)
builder.add_node("process", process_query)
builder.add_node("output", generate_output)

builder.set_entry_point("retrieve")
builder.add_edge("retrieve", "process")
builder.add_edge("process", "output")

graph = builder.compile()

# ---------------- FUNCTION ----------------
def run_query(query):
    result = graph.invoke({
        "query": query,
        "context": "",
        "answer": "",
        "escalate": False
    })
    return result["answer"]

# ---------------- TEST ----------------
if __name__ == "__main__":
    while True:
        q = input("Ask: ")
        print(run_query(q))
