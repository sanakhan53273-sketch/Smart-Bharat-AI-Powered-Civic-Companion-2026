from flask import Flask, render_template, request
import random

app = Flask(__name__)

government_services = {
    "aadhaar": {
        "title": "Aadhaar Card",
        "answer": "You can apply at your nearest Aadhaar Enrollment Centre or online through UIDAI.",
        "documents": "Proof of Identity, Proof of Address, Date of Birth Proof"
    },
    "pan": {
        "title": "PAN Card",
        "answer": "Apply online through the Income Tax Portal.",
        "documents": "Aadhaar Card, Address Proof, Passport-size Photo"
    },
    "passport": {
        "title": "Passport",
        "answer": "Apply online through Passport Seva Portal and book an appointment.",
        "documents": "Aadhaar Card, Birth Certificate, Address Proof"
    },
    "pm kisan": {
        "title": "PM Kisan",
        "answer": "Eligible farmers can register under PM Kisan Scheme.",
        "documents": "Aadhaar, Bank Passbook, Land Records"
    },
    "ayushman": {
        "title": "Ayushman Bharat",
        "answer": "Check eligibility and apply online.",
        "documents": "Aadhaar Card, Ration Card"
    }
}


@app.route("/", methods=["GET", "POST"])
def home():

    response = ""
    complaint_id = ""
    language = "English"

    if request.method == "POST":

        language = request.form.get("language", "English")

        # AI Query
        if "query" in request.form:

            query = request.form["query"].lower()

            found = False

            for key in government_services:

                if key in query:

                    service = government_services[key]

                    if language == "Hindi":

                        response = f"""
सेवा : {service['title']}

जानकारी :
{service['answer']}

आवश्यक दस्तावेज़ :
{service['documents']}

स्थिति :
आप इस सेवा के लिए ऑनलाइन आवेदन कर सकते हैं।
"""

                    else:

                        response = f"""
Service : {service['title']}

Information :
{service['answer']}

Required Documents :
{service['documents']}

Status :
You can apply online for this service.
"""

                    found = True
                    break

            if not found:

                if language == "Hindi":
                    response = "माफ़ कीजिए, यह सेवा उपलब्ध नहीं मिली।"
                else:
                    response = "Sorry! Service not found."

        # Complaint
        elif "issue" in request.form:

            name = request.form["name"]
            issue = request.form["issue"]

            complaint_id = "SB" + str(random.randint(100000,999999))

    return render_template(
        "index.html",
        response=response,
        complaint_id=complaint_id,
        language=language
    )


@app.route("/health")
def health():
    return "Application Running Successfully"


if __name__ == "__main__":
    app.run(debug=True)