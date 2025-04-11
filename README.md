# ⚖️ CLAT Legal Exam Chatbot

This project provides an NLP-powered chatbot to answer CLAT-related queries using a **hybrid approach**:
- A local knowledge base for quick and relevant responses
- Fallback to web search (via SerpAPI) when the local knowledge base doesn't have a confident match

Built using `spaCy` for semantic similarity and `Streamlit` for an interactive web interface.

---

##  Features

-  Answers frequently asked CLAT questions
-  Uses **semantic similarity** with `spaCy`
-  **Hybrid model**: Local knowledge base + Web fallback via SerpAPI
-  Streamlit-based chatbot interface
-  Easily extensible — just update `knowledge_base.json`

---

## How to Run

### 1. Install Dependencies

```bash
pip install -r requirements.txt
python -m spacy download en_core_web_md
```

---

### 2. Add Your SerpAPI Key

This project uses [SerpAPI](https://serpapi.com) to search the web when local answers aren't sufficient.

> ⚠️ **Important**: Use your **own SerpAPI key**.  
> The developer key used during testing has usage limits.

In `streamlit_chatbot.py`, replace this line:

```python
api_key = "YOUR_SERPAPI_KEY"
```

---

### 3. Run from Command Line

```bash
python chatbot_clat_queries.py
```

---

### 4. Run with Streamlit (Web App)

```bash
streamlit run streamlit_chatbot.py
```

---

## 💬 Sample Questions

Try asking:

- What is the syllabus for CLAT 2026?
- How many questions are there in the English section?
- Give me last year’s cut-off for NLSIU Bangalore.
- How many seats are there in NALSAR Hyderabad?
- What is the marking scheme in CLAT?

---

## 📁 Project Structure

```
📂 CLAT-Chatbot/
├── knowledge_base.json           # Local Q&A database
├── chatbot_clat_queries.py       # CLI version of chatbot
├── streamlit_chatbot.py          # Streamlit web app (hybrid version)
├── requirements.txt              # Python dependencies
└── README.md                     # Project documentation (this file)
```

---

## 🔄 Future Scope

- Improve local matching using Sentence-BERT or dense retrieval
- Store unanswered queries and user feedback to grow KB
- Add citations and links in web search results
- Upgrade to GPT-based model using fine-tuned NLTI data
- Integrate vector databases like FAISS for scalability

---

✅ Built to support law aspirants with AI-powered legal exam preparation tools.