# ✅ test_chat.py
from hf_prompt_generator import generate_prompts
from chat_engine import start_conversation

# Sample fields used in JotForm
fields = [
    {"name": "q3_name[first]", "type": "text"},
    {"name": "q3_name[last]", "type": "text"},
    {"name": "q4_email", "type": "email"},
    {"name": "q5_aadhaarNumber", "type": "text"},
    {"name": "gender", "type": "text"},
    {"name": "lang_pref", "type": "text"},
]

# Generate prompts using HF model
all_fields = generate_prompts(fields)
print("\n🔎 Prompt Output:", all_fields)

# Filter valid ones with 'question'
sample_fields = [item for item in all_fields if "question" in item]

# Start the chatbot conversation
start_conversation(sample_fields)