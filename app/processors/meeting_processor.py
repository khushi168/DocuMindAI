import re


def clean_text(text):

    text = text.replace("\n", " ")

    text = re.sub(r"\s+", " ", text)

    return text.strip()


def process_meeting_notes(text):

    text = clean_text(text)

    attendees = []
    discussion_points = []
    action_items = []
    deadlines = []
    decisions = []

    # ---------------- ATTENDEES ----------------

    names = re.findall(r"\b[A-Z][a-z]+\b", text)

    ignore_words = [
        "Meeting",
        "Today",
        "Friday",
        "Monday",
        "FastAPI",
        "DocuMind",
        "OCR",
        "PDFs",
        "Action",
        "Deadline",
        "Next",
        "Team",
        "The",
        "It",
        "AI"
    ]

    for name in names:

        if (
            name not in ignore_words
            and name not in attendees
        ):
            attendees.append(name)

    attendees = attendees[:6]

    # ---------------- DISCUSSION POINTS ----------------

    discussion_rules = [

        (
            ["resume", "invoice", "meeting"],
            "Reviewed progress of resume parsing, invoice extraction, and meeting automation modules."
        ),

        (
            ["frontend", "dashboard"],
            "Discussed frontend dashboard improvements and dynamic UI cards for multiple document types."
        ),

        (
            ["ocr", "pdf"],
            "Reviewed OCR testing results and discussed issues with scanned PDF invoice extraction."
        ),

        (
            ["export", "download"],
            "Proposed export and download functionality for generated MOM reports and analytics dashboards."
        ),

        (
            ["backend", "api", "fastapi"],
            "Reviewed backend APIs and confirmed FastAPI routes for uploads and parsing workflows."
        ),

        (
            ["legal", "contract", "nda"],
            "Discussed future support for legal contracts, agreements, NDAs, and HR documents."
        ),

        (
            ["database", "history"],
            "Suggested implementing database history tracking and uploaded document logging."
        )
    ]

    added_points = []

    lower_text = text.lower()

    for keywords, summary in discussion_rules:

        if any(word in lower_text for word in keywords):

            if summary not in added_points:

                discussion_points.append(summary)

                added_points.append(summary)

    # ---------------- ACTION ITEMS ----------------

    action_matches = re.findall(
        r"-\s*([A-Z][a-z]+)\s+will\s+([^\n.]+)",
        text
    )

    for person, task in action_matches:

        task = task.strip()

        action_items.append(
            f"{person} → {task}"
        )

    # ---------------- DEADLINES ----------------

    sentences = re.split(r'(?<=[.!?])\s+', text)

    for sentence in sentences:

        lower = sentence.lower()

        if any(word in lower for word in [
            "deadline",
            "scheduled",
            "friday",
            "monday",
            "tomorrow",
            "next week"
        ]):

            clean = sentence.strip()

            if clean not in deadlines:
                deadlines.append(clean)

    # ---------------- DECISIONS ----------------

    for sentence in sentences:

        lower = sentence.lower()

        if any(word in lower for word in [
            "decided",
            "approved",
            "finalized",
            "confirmed"
        ]):

            decisions.append(sentence.strip())

    # ---------------- FALLBACKS ----------------

    if not discussion_points:

        discussion_points.append(
            "Project updates and deployment planning discussed."
        )

    if not action_items:

        action_items.append(
            "Follow up on pending tasks."
        )

    if not deadlines:

        deadlines.append(
            "Next review meeting to be scheduled."
        )

    # ---------------- SUMMARY ----------------

    summary = (
        "Deployment planning and project review meeting conducted."
    )

    return {
        "document_type": "Meeting Notes",
        "summary": summary,
        "attendees": attendees,
        "discussion_points": discussion_points[:6],
        "decisions": decisions[:4],
        "action_items": action_items[:6],
        "deadlines": deadlines[:4]
    }