from flask import Flask, request, jsonify
from flask_cors import CORS
import os
import traceback
import requests

from form_parser import parse_form, fetch_html_from_url
from prompt_generator import generate_prompts
from chat_engine import start_conversation
from form_filler import fill_form
from translator import translate_text  # ✅ Now using Deep Translator backend

app = Flask(__name__)
CORS(app)

UPLOAD_FOLDER = "static"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def home():
    return "✅ Form-to-Convo Backend is running!"

# 1️⃣ Upload HTML file → extract fields & generate prompts
@app.route('/generate-prompts', methods=['POST'])
def generate_prompt():
    try:
        if 'form' not in request.files:
            print("❌ No file uploaded.")
            return jsonify({'error': 'No file uploaded'}), 400

        html_file = request.files['form']
        filename = html_file.filename
        path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        html_file.save(path)
        print(f"📥 Saved uploaded file to: {path}")

        with open(path, 'r', encoding='utf-8') as f:
            html = f.read()

        print(f"📄 HTML size: {len(html)} characters")

        fields = parse_form(html)
        if not fields:
            print("❌ No fields extracted from the HTML.")
            return jsonify({'error': 'No form fields found in the HTML.'}), 400

        prompts = generate_prompts(fields)
        print(f"✅ Generated {len(prompts)} prompts.")
        return jsonify({'fields': fields, 'prompts': prompts})

    except Exception as e:
        traceback.print_exc()
        return jsonify({'error': f'Prompt generation failed: {str(e)}'}), 500

# 2️⃣ Parse a live form URL → extract fields & generate prompts
@app.route('/parse_url', methods=['POST'])
def parse_url():
    try:
        data = request.get_json()
        url = data.get("url")
        if not url:
            return jsonify({'error': 'No URL provided'}), 400

        response = requests.get(url, timeout=10)
        response.raise_for_status()
        html = response.text

        fields = parse_form(html)
        prompts = generate_prompts(fields)
        return jsonify({'fields': fields, 'prompts': prompts})

    except Exception as e:
        traceback.print_exc()
        return jsonify({'error': f'URL parsing failed: {str(e)}'}), 500

# 3️⃣ Translate list of prompts to desired language
@app.route('/translate-prompts', methods=['POST'])
def translate_prompts():
    try:
        data = request.get_json()
        prompts = data.get("prompts", [])
        lang = data.get("lang", "en")

        translated = []
        for p in prompts:
            question = p.get("question", "")
            if lang != "en" and question:
                question = translate_text(question, dest_lang=lang)
            translated.append({**p, "question": question})

        return jsonify({'prompts': translated})

    except Exception as e:
        traceback.print_exc()
        return jsonify({'error': f'Translation failed: {str(e)}'}), 500

# 4️⃣ Run conversation in CLI (or future web chat)
@app.route('/start-chat', methods=['POST'])
def start_chat():
    try:
        data = request.get_json()
        prompts = data.get("prompts", [])
        responses = start_conversation(prompts)
        return jsonify({'responses': responses})

    except Exception as e:
        traceback.print_exc()
        return jsonify({'error': f'Conversation failed: {str(e)}'}), 500

# 5️⃣ Auto-fill & submit using Selenium
@app.route('/fill-form', methods=['POST'])
def auto_fill():
    try:
        data = request.get_json()
        url = data.get("form_url")
        responses = data.get("responses", {})

        if not url or not responses:
            return jsonify({'error': 'Missing form_url or responses'}), 400

        fill_form(url, responses)
        return jsonify({'message': 'Form filled and submitted ✅'})

    except Exception as e:
        traceback.print_exc()
        return jsonify({'error': f'Auto-fill failed: {str(e)}'}), 500

if __name__ == "__main__":
    app.run(port=5000, debug=True)
