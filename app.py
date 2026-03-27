from fastapi import FastAPI
import pickle
import re

# app create
app = FastAPI()

# load model + vectorizer
model = pickle.load(open("model.pkl", "rb"))
vectorizer = pickle.load(open("tfidf.pkl", "rb"))

# clean function
def clean_text(text):
    text = text.lower()
    text = re.sub(r'[^a-zA-Z ]', '', text)
    return text

# priority function
def get_priority(text):
    text = text.lower()
    
    if "urgent" in text or "hacked" in text:
        return "High"
    elif "failed" in text or "not working" in text:
        return "Medium"
    else:
        return "Low"

# main prediction API
@app.get("/")
def home():
    return {"message": "API is running 🚀"}

@app.get("/predict")
def predict(text: str):
    clean = clean_text(text)
    vec = vectorizer.transform([clean])
    
    category = model.predict(vec)[0]
    priority = get_priority(clean)
    
    return {
        "category": category,
        "priority": priority
    }