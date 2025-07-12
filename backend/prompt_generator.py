# prompt_generator.py

def generate_prompt(field):
    field_type = field.get("type", "text")
    label = field.get("label") or field.get("name") or "this field"
    label = label.strip().replace("_", " ").capitalize()

    # Basic rule-based prompt generation
    if field_type in ["text", "email", "password", "textarea"]:
        return f"What is your {label}?"
    elif field_type == "number":
        return f"Please enter a number for your {label}."
    elif field_type == "date":
        return f"When is your {label}?"
    elif field_type == "select" and field.get("options"):
        options = ", ".join(field["options"][:4])  # show top 4 options
        return f"Please select your {label}. Options include: {options}."
    elif field_type == "radio":
        return f"Which option would you like to select for {label}?"
    elif field_type == "checkbox":
        return f"Do you want to enable {label}?"
    else:
        return f"Please provide your {label}."


def generate_prompts(fields):
    prompts = []
    for field in fields:
        question = generate_prompt(field)
        prompts.append({
            "field_name": field.get("name"),
            "question": question
        })
    return prompts
