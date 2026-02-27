from parser import parse_resume
from validator import validate_email, validate_phone, check_timeline
from fraud import calculate_score

print("Paste resume text and press Enter:\n")
text = input()

data = parse_resume(text)

data["email_valid"] = validate_email(data["email"])
data["phone_valid"] = validate_phone(data["phone"])
data["timeline_ok"] = check_timeline(data["dates"])

score, flags = calculate_score(data)

print("\n--- FRAUD REPORT ---")
print("Fraud Score:", score)
print("Flags:", flags)