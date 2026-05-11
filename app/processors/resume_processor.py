import re

def process_resume(text):

    email = re.search(
        r'[\w\.-]+@[\w\.-]+',
        text
    )

    phone = re.search(
        r'\+?\d[\d\s-]{8,}',
        text
    )

    lines = text.split("\n")

    name = "Not Found"

    for line in lines:

        clean_line = line.strip()

        if (
            len(clean_line) > 3
            and len(clean_line) < 40
            and "@" not in clean_line
            and not any(char.isdigit() for char in clean_line)
        ):

            name = clean_line
            break

    skill_keywords = [
        "Python",
        "SQL",
        "FastAPI",
        "Machine Learning",
        "Data Analysis",
        "Pandas",
        "NumPy",
        "Power BI",
        "React",
        "PostgreSQL"
    ]

    detected_skills = []

    for skill in skill_keywords:

        if skill.lower() in text.lower():

            detected_skills.append(skill)

    projects = []

    ignore_words = [
        "project",
        "projects",
        "education",
        "skills",
        "experience"
    ]

    for line in lines:

        clean_line = line.strip()

        if len(clean_line) < 25:
            continue

        if clean_line.lower() in ignore_words:
            continue

        if (
            "developed" in clean_line.lower()
            or "built" in clean_line.lower()
            or "created" in clean_line.lower()
            or "system" in clean_line.lower()
            or "application" in clean_line.lower()
            or "platform" in clean_line.lower()
            or "analyzer" in clean_line.lower()
        ):

            projects.append(clean_line)

    data = {

        "document_type": "Resume",

        "name":
            name,

        "email":
            (
                email.group(0)
                if email else "Not Found"
            ),

        "phone":
            (
                phone.group(0)
                if phone else "Not Found"
            ),

        "skills":
            detected_skills,

        "projects":
            projects[:5],

        "actions": [
            "Review candidate profile",
            "Schedule technical interview",
            "Evaluate project experience"
        ]
    }

    return data