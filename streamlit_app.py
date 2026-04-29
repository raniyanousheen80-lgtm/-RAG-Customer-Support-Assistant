import streamlit as st
from app import run_query

# Page config
st.set_page_config(page_title="AI Support Assistant", page_icon="🤖")

st.title("🤖 AI Customer Support Assistant")
st.caption("RAG + LangGraph + HITL System")

# Sidebar
st.sidebar.title("ℹ️ About")
st.sidebar.info(
    "This assistant uses a RAG-based system with LangGraph workflow and supports Human-in-the-Loop escalation."
)

# Chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display messages
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Input
query = st.chat_input("Ask your question...")

if query:
    # User message
    st.session_state.messages.append({"role": "user", "content": query})
    with st.chat_message("user"):
        st.markdown(query)

    # Get response
    answer = run_query(query)

    # Bot response
    with st.chat_message("assistant"):
        if "Escalated" in answer:
            st.error(answer)
        else:
            st.success(answer)

    st.session_state.messages.append({"role": "assistant", "content": answer})