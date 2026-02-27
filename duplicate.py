import json
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

DB_FILE = "database.json"

def load_db():
    with open(DB_FILE, "r") as f:
        return json.load(f)

def save_db(data):
    with open(DB_FILE, "w") as f:
        json.dump(data, f, indent=2)

def check_duplicate(new_resume):
    db = load_db()

    # Check email/phone match
    for r in db:
        if r["email"] == new_resume["email"]:
            return True, "Duplicate email detected"
        if r["phone"] == new_resume["phone"]:
            return True, "Duplicate phone detected"

    # Check text similarity
    texts = [r["text"] for r in db] + [new_resume["text"]]

    if len(texts) > 1:
        vect = TfidfVectorizer().fit_transform(texts)
        sim = cosine_similarity(vect[-1], vect[:-1])

        if sim.max() > 0.8:
            return True, "Similar resume already exists"

    return False, None

def add_resume(data):
    db = load_db()
    db.append(data)
    save_db(db)