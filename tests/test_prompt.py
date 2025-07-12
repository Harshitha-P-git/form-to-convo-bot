from form_parser import fetch_html_from_url, parse_form
from prompt_generator import generate_prompts
from pprint import pprint

# ✅ Step 1: Set the local form URL (update if different)
url = "http://localhost:8000/form_wizard.html"

# ✅ Step 2: Fetch and parse the form
html = fetch_html_from_url(url)
fields = parse_form(html)

# ✅ Step 3: Generate natural language prompts
questions = generate_prompts(fields)

# ✅ Step 4: Display questions
pprint(questions)
