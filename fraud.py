def calculate_score(data):
    score = 0
    flags = []

    # Email validation
    if not data.get("email_valid"):
        score += 25
        flags.append("Invalid Email")

    # Phone validation
    if not data.get("phone_valid"):
        score += 25
        flags.append("Invalid Phone")

    # Timeline consistency
    if not data.get("timeline_ok"):
        score += 20
        flags.append("Suspicious experience timeline")

    # Duplicate detection
    if data.get("duplicate"):
        score += 40
        if data.get("dup_reason"):
            flags.append(data.get("dup_reason"))
        else:
            flags.append("Duplicate profile detected")

    # Resume length check
    text = data.get("text", "")
    if len(text) < 200:
        score += 10
        flags.append("Very short resume")

    # Fake experience patterns
    exp_flags = data.get("experience_flags", [])
    if exp_flags:
        score += 30
        flags.extend(exp_flags)

    return score, flags