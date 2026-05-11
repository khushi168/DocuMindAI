def classify_document(text):

    text = text.lower()

    # OFFER LETTER

    if (
        "offer letter" in text
        or "joining date" in text
        or "employment bond" in text
        or "ctc" in text
        or "compensation revision" in text
    ):

        return "Offer Letter"

    # MEETING NOTES

    elif (
        "meeting summary" in text
        or "discussion points" in text
        or "action items" in text
        or "attendees" in text
        or "meeting notes" in text
    ):

        return "Meeting Notes"

    # RESUME

    elif (
        "skills" in text
        or "education" in text
        or "projects" in text
        or "experience" in text
        or "certifications" in text
    ):

        return "Resume"

    # INVOICE

    elif (
        "invoice no" in text
        or "due date" in text
        or "grand total" in text
        or "issued to" in text
        or "bank name" in text
    ):

        return "Invoice"

    return "General Document"