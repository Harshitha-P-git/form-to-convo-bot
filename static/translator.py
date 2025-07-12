from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import torch

tokenizer = AutoTokenizer.from_pretrained(
    "ai4bharat/indictrans2-en-indic-dist-200M", trust_remote_code=True
)
model = AutoModelForSeq2SeqLM.from_pretrained(
    "ai4bharat/indictrans2-en-indic-dist-200M", trust_remote_code=True
)

# Correct tag mapping
LANG_TAGS = {
    "en": "eng_Latn",
    "hi": "hin_Deva",
    "te": "tel_Telu",
    "ta": "tam_Taml",
    "kn": "kan_Knda",
    "ml": "mal_Mlym",
    "bn": "ben_Beng",
    "gu": "guj_Gujr",
    "mr": "mar_Deva",
    "pa": "pan_Guru",
    "ur": "urd_Arab",
    "or": "ory_Orya",
}

def translate_text(text, src_lang="en", dest_lang="hi"):
    src_tag = LANG_TAGS.get(src_lang)
    tgt_tag = LANG_TAGS.get(dest_lang)

    if not src_tag or not tgt_tag:
        raise ValueError(f"Invalid language tags: {src_lang}, {dest_lang}")

    # ✅ Set tokenizer's src and target language before encoding
    tokenizer.src_lang = src_tag
    tokenizer.tgt_lang = tgt_tag

    inputs = tokenizer(text, return_tensors="pt", padding=True)

    with torch.no_grad():
        output = model.generate(**inputs, max_length=128)

    translated = tokenizer.batch_decode(output, skip_special_tokens=True)
    return translated[0]
