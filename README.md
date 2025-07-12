# 🧠 Form-to-Convo Bot

A smart tool that transforms any HTML form (including multi-step wizard-style forms) into a multilingual conversational chatbot. The chatbot asks users for their inputs, validates them, translates the prompts if needed, and auto-fills the original form via Selenium.

---

## 📌 Features

- ✅ Upload or fetch HTML forms from a URL
- ✅ Extract fields using BeautifulSoup
- ✅ Generate conversational prompts
- ✅ Translate prompts using IndicTrans2 (Hindi, Telugu, Tamil, Kannada)
- ✅ Collect user inputs through a chatbot (React)
- ✅ Auto-fill and submit the original form using Selenium
- ✅ Supports multilingual input/output

---

## 🛠 Tech Stack

| Part         | Tech Used                     |
|--------------|-------------------------------|
| Frontend     | React                         |
| Backend      | Flask + Python                |
| HTML Parsing | BeautifulSoup                 |
| Translation  | IndicTrans2 (HuggingFace)     |
| Automation   | Selenium                      |
| LLM Prompts  | HuggingFace Transformers      |

---

## 🚀 Run Instructions

### 1. Backend (Flask)
```bash
cd backend
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python app.py
```

2. Frontend (React)
```bash
cd frontend
npm install
npm start
```

3. Open the App
   
  Visit: http://localhost:3000
