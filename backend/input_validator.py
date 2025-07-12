import re

def is_valid_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return bool(re.match(pattern, email))

def is_valid_aadhaar(aadhaar):
    return aadhaar.isdigit() and len(aadhaar) == 12

def mask_email(email):
    try:
        name, domain = email.split('@')
        masked = name[0] + "***@" + domain
        return masked
    except:
        return email

def mask_aadhaar(aadhaar):
    return "XXXXXX" + aadhaar[-4:] if len(aadhaar) == 12 else aadhaar
