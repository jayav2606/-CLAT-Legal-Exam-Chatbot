import streamlit as st
import json
import spacy
import requests

nlp = spacy.load("en_core_web_md")

# Load local knowledge base
with open("knowledge_base.json", "r") as f:
    knowledge_base = json.load(f)

# SerpAPI search (fallback)
def search_serpapi(query):
    api_key = "YOUR_SERPAPI_KEY"  # Replace with your key
    url = "https://serpapi.com/search"
    params = {
        "q": query,
        "engine": "google",
        "api_key": '9dca3b6539ba2136ebf0c89664e9c27cef6fbcec5a6d11ccb40800d03d77c3a9'
    }
    response = requests.get(url, params=params)
    results = response.json()
    snippets = []
    for result in results.get("organic_results", []):
        if "snippet" in result:
            snippets.append(result["snippet"])
    return "\n\n".join(snippets[:3]) if snippets else "Sorry, I couldn't find anything online either."

# Search local KB with similarity threshold
def get_best_answer(user_query, threshold=0.75):
    user_doc = nlp(user_query)
    best_score = -1
    best_answer = None

    for item in knowledge_base:
        question_doc = nlp(item['question'])
        score = user_doc.similarity(question_doc)
        if score > best_score:
            best_score = score
            best_answer = item['answer']

    if best_score >= threshold:
        return best_answer
    else:
        return None  # Fallback to web

# Streamlit UI
st.set_page_config(page_title="CLAT Chatbot", page_icon="⚖️")
st.title("🤖 CLAT Legal Exam Chatbot")
st.write("Ask anything about CLAT preparation, syllabus, cutoffs, and more.")

query = st.text_input("Your Question:")

if query:
    answer = get_best_answer(query)
    if answer:
        st.markdown(f"**Answer (from Knowledge Base):** {answer}")
    else:
        st.markdown("🔍 Searching online...")
        web_answer = search_serpapi(query)
        st.markdown(f"**Answer (from Web):** {web_answer}")
