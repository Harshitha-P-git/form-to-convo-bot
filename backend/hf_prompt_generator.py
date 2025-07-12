# hf_prompt_generator.py

from transformers import pipeline
import os
from dotenv import load_dotenv

load_dotenv()
HF_TOKEN = os.getenv("HF_TOKEN")

generator = pipeline(
    "text2text-generation",
    model="google/flan-t5-large",
    token=HF_TOKEN
)

def generate_prompts(fields):
    prompts = []
    for field in fields:
        name = field.get("name")
        ftype = field.get("type", "text")

        input_text = f"Generate a simple and clear question for input field: '{name}' of type '{ftype}'"
        try:
            response = generator(input_text, max_new_tokens=50)
            question = response[0]["generated_text"].strip()

            if question:
                prompts.append({"field_name": name, "question": question})
            else:
                prompts.append({"field_name": name, "error": "No question generated"})
        except Exception as e:
            prompts.append({"field_name": name, "error": str(e)})
    
    return prompts
