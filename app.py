from flask import Flask, render_template, request

app = Flask(__name__)

government_services = {
    "aadhaar": {
        "answer": "You can apply for Aadhaar at your nearest Aadhaar Enrollment Centre.",
        "documents": "Proof of Identity, Proof of Address, Date of Birth Proof."
    },
    "pan": {
        "answer": "You can apply for a PAN Card online through the Income Tax portal.",
        "documents": "Aadhaar Card, Address Proof, Passport-size Photo."
    },
    "passport": {
        "answer": "Apply online through the Passport Seva Portal and book an appointment.",
        "documents": "Aadhaar Card, Birth Certificate, Address Proof."
    },
    "pm kisan": {
        "answer": "Eligible farmers can register under the PM Kisan Scheme.",
        "documents": "Aadhaar, Bank Passbook, Land Records."
    },
    "ayushman": {
        "answer": "Check your eligibility for Ayushman Bharat and apply online.",
        "documents": "Aadhaar Card, Ration Card (if applicable)."
    }
}

@app.route("/", methods=["GET", "POST"])
def home():
    response = ""
    complaint_id = ""

    if request.method == "POST":

        # AI Chat
        if "query" in request.form:
            query = request.form["query"].lower()

            found = False

            for key in government_services:
                if key in query:
                    service = government_services[key]
                    response = f"""
Service: {key.title()}

Answer:
{service['answer']}

Required Documents:
{service['documents']}
"""
                    found = True
                    break

            if not found:
                response = "Sorry, I couldn't find the requested government service."

        # Complaint Form
        elif "issue" in request.form:
            name = request.form["name"]
            issue = request.form["issue"]

            complaint_id = "SB2026" + str(len(name) + len(issue) + 1000)

    return render_template(
        "index.html",
        response=response,
        complaint_id=complaint_id
    )

if __name__ == "__main__":
    app.run(debug=True)