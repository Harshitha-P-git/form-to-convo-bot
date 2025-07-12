from hf_prompt_generator import generate_prompts

form_fields = [
    {"name": "name", "label": "Enter your full name"},
    {"name": "email", "label": "Enter your email address"},
    {"name": "dob", "label": "Enter your date of birth"},
]

print("🔍 Generating prompts using Hugging Face model...")
prompts = generate_prompts(form_fields)
for item in prompts:
    print(item)
