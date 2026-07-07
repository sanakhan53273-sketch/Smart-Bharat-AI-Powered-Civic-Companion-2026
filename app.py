from flask import Flask, render_template, request
import random

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
    },
    "driving licence": {
        "answer": "Apply through the Parivahan Portal for a Driving Licence.",
        "documents": "Aadhaar Card, Address Proof, Passport-size Photo."
    },
    "voter id": {
        "answer": "Apply through the Election Commission Portal.",
        "documents": "Aadhaar Card, Address Proof, Passport-size Photo."
    },
    "ration card": {
        "answer": "Apply through your State Food and Civil Supplies Portal.",
        "documents": "Identity Proof, Address Proof, Family Details."
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
🏛 Service: {key.title()}

✅ Answer:
{service['answer']}

📄 Required Documents:
{service['documents']}
"""

                    found = True
                    break

            if not found:
                response = """
❌ Sorry!

I couldn't find the requested government service.

Try searching for:
• Aadhaar
• PAN Card
• Passport
• PM Kisan
• Ayushman Bharat
• Driving Licence
• Voter ID
• Ration Card
"""

        # Complaint Form
        elif "issue" in request.form:
            name = request.form["name"]
            issue = request.form["issue"]

            complaint_id = f"SB2026{random.randint(100000,999999)}"

    return render_template(
        "index.html",
        response=response,
        complaint_id=complaint_id
    )


if __name__ == "__main__":
    app.run(debug=True)