import re

def parse_resume(text):
    email = re.findall(r'\S+@\S+', text)
    phone = re.findall(r'\b\d{10}\b', text)
    dates = re.findall(r'(20\d{2})', text)

    return {
        "email": email[0] if email else None,
        "phone": phone[0] if phone else None,
        "dates": dates,
        "text": text
    }