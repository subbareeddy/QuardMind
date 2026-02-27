def validate_email(email):
    return bool(email and "@" in email)

def validate_phone(phone):
    return bool(phone and len(phone) == 10)

def check_timeline(dates):
    years = list(map(int, dates))
    return sorted(years) == years