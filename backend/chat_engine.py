from translator import translate_text, reverse_translate_text
from input_validator import is_valid_email, is_valid_aadhaar, mask_email, mask_aadhaar

def start_conversation(prompts):
    responses = {}

    print("\n🌐 Available Languages: en (English), hi (Hindi), te (Telugu), ta (Tamil), kn (Kannada)")
    lang_code = input("🔤 Choose your language (e.g., 'hi' for Hindi): ").strip().lower()

    print("\n🤖 Starting chat in your language...\n")

    for item in prompts:
        field = item.get("field_name")
        question = item.get("question")

        if not question:
            print(f"⚠️ Skipping field '{field}' due to missing or invalid question.")
            continue

        # 🌐 Translate question
        try:
            translated_q = translate_text(question, dest_lang=lang_code)
        except Exception:
            translated_q = question  # fallback to original if translation fails

        print(f"🗨️ {translated_q}")

        while True:
            user_input = input("👤 Your Answer: ").strip()

            # 🔁 Reverse-translate to English for validation
            try:
                english_input = reverse_translate_text(user_input, src_lang=lang_code)
            except Exception:
                english_input = user_input  # fallback if reverse translation fails

            # 🎯 Aadhaar validation
            if "aadhaar" in field.lower() and not is_valid_aadhaar(english_input):
                print("⚠️ Invalid Aadhaar. Please enter a 12-digit number.")
                continue

            # 📧 Email validation
            if "email" in field.lower() and not is_valid_email(english_input):
                print("⚠️ Invalid Email. Please enter a valid email address.")
                continue

            # 🔐 Apply masking
            if "aadhaar" in field.lower():
                english_input = mask_aadhaar(english_input)
            if "email" in field.lower():
                english_input = mask_email(english_input)

            responses[field] = english_input
            break

    print("\n✅ All responses collected (masked if sensitive):")
    print(responses)
