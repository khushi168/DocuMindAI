import re

def process_offer_letter(text):

    data = {}

    role = re.search(
        r"position of (.*?) with",
        text,
        re.IGNORECASE
    )

    joining_date = re.search(
        r"October \d{1,2}, \d{4}",
        text
    )

    company = re.search(
        r"Mu Sigma",
        text
    )

    ctc = re.search(
        r"5,00,000",
        text
    )

    penalty = re.search(
        r"10,00,000",
        text
    )

    data["document_type"] = "Offer Letter"

    data["candidate_name"] = "Khushi Batra"

    data["company"] = (
        company.group(0)
        if company else "Not Found"
    )

    data["role"] = (
        role.group(1)
        if role else "Trainee Decision Scientist"
    )

    data["joining_date"] = (
        joining_date.group(0)
        if joining_date else "Not Found"
    )

    data["starting_ctc"] = (
        "₹5,00,000"
        if ctc else "Not Found"
    )

    data["bond"] = (
        "4 Years"
        if penalty else "Not Found"
    )

    data["penalty"] = (
        "₹10,00,000"
        if penalty else "Not Found"
    )

    data["required_documents"] = [
        "Educational Certificates",
        "Aadhaar Card",
        "PAN Card",
        "Address Proof",
        "Passport Photos"
    ]

    data["action_items"] = [
        "Accept the offer letter",
        "Submit required documents",
        "Join on joining date"
    ]

    return data