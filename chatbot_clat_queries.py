import json
import spacy

nlp = spacy.load("en_core_web_md")

with open("knowledge_base.json", "r") as f:
    knowledge_base = json.load(f)

def get_best_answer(user_query):
    user_doc = nlp(user_query)
    best_score = -1
    best_answer = "Sorry, I couldn't find an answer to that. Please try rephrasing."

    for item in knowledge_base:
        question_doc = nlp(item['question'])
        score = user_doc.similarity(question_doc)
        if score > best_score:
            best_score = score
            best_answer = item['answer']

    return best_answer

if __name__ == "__main__":
    print("CLAT Chatbot (type 'exit' to quit)")
    while True:
        query = input("You: ")
        if query.lower() == 'exit':
            break
        response = get_best_answer(query)
        print("Bot:", response)