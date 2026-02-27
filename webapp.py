from flask import Flask, render_template, request
from parser import parse_resume
from validator import validate_email, validate_phone, check_timeline
from fraud import calculate_score
from duplicate import check_duplicate, add_resume
from experience import check_experience_patterns

app = Flask(__name__)

# 🔹 Dashboard page
@app.route("/")
def dashboard():
    return render_template("dashboard.html")

# 🔹 Resume upload page
@app.route("/upload", methods=["GET","POST"])
def upload():
    result = None

    if request.method == "POST":
        file = request.files.get("resume")

        if file and file.filename != "":
            text = file.read().decode("utf-8", errors="ignore")
        else:
            text = ""

        data = parse_resume(text)
        data["text"] = text

        data["email_valid"] = validate_email(data.get("email"))
        data["phone_valid"] = validate_phone(data.get("phone"))
        data["timeline_ok"] = check_timeline(data.get("dates", []))

        dup, reason = check_duplicate(data)
        data["duplicate"] = dup
        data["dup_reason"] = reason
        if not dup:
            add_resume(data)

        data["experience_flags"] = check_experience_patterns(data.get("dates", []))

        score, flags = calculate_score(data)

        result = {
            "score": score,
            "flags": flags,
            "duplicate": data["duplicate"],
            "experience_flags": data["experience_flags"]
        }

    return render_template("upload.html", result=result)

# 🔹 API documentation page
@app.route("/api")
def api_docs():
    return render_template("api.html")

if __name__ == "__main__":
    app.run(debug=True)