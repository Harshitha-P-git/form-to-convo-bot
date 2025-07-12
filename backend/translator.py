from deep_translator import GoogleTranslator

# Mapping of language selection to ISO 639-1 language codes
LANG_CODES = {
    "en": "en",
    "hi": "hi",
    "te": "te",
    "ta": "ta",
    "kn": "kn"
}

# 🔄 English → Indic (or any other)
def translate_text(text, dest_lang="hi"):
    if dest_lang == "en" or not text.strip():
        return text

    lang_code = LANG_CODES.get(dest_lang)
    if not lang_code:
        print(f"[Translation Error] Unsupported target language: {dest_lang}")
        return text

    try:
        translated = GoogleTranslator(source="auto", target=lang_code).translate(text)
        print(f"🌐 Translated to [{lang_code}]: {translated}")
        return translated
    except Exception as e:
        print(f"[Translation Error] {e}")
        return text  # fallback to original


# 🔄 Indic → English (if needed)
def reverse_translate_text(text, src_lang="hi"):
    if not text.strip():
        return text

    lang_code = LANG_CODES.get(src_lang, "auto")

    try:
        translated = GoogleTranslator(source=lang_code, target="en").translate(text)
        print(f"🔁 Reverse-translated to [en]: {translated}")
        return translated
    except Exception as e:
        print(f"[Reverse Translation Error] {e}")
        return text
