# NLP Ticket Classifier

This project is an end-to-end NLP-based ticket classification system.

## Features
- Classifies support tickets into:
  - Billing
  - Technical
  - Login Issue
  - Security
  - Delivery
  - Query
- Uses TF-IDF + Naive Bayes
- FastAPI backend
- Streamlit frontend

## How to Run

### 1. Install dependencies
pip install -r requirements.txt

### 2. Run FastAPI
uvicorn app:app --reload

### 3. Run Streamlit
streamlit run ui.py

## Tech Stack
- Python
- Scikit-learn
- FastAPI
- Streamlit
