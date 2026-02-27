def check_experience_patterns(dates):
    flags = []

    years = list(map(int, dates))

    # Rule 1: Too many jobs in short period
    if len(years) > 6:
        flags.append("Too many job entries detected")

    # Rule 2: Unrealistic fast career (many years in small range)
    if years:
        if max(years) - min(years) < 2 and len(years) > 3:
            flags.append("Unrealistic rapid career growth")

    # Rule 3: Duplicate year entries (copy-paste pattern)
    if len(set(years)) != len(years):
        flags.append("Repeated experience years detected")

    return flags