from fastapi import (
    FastAPI,
    Request,
    UploadFile,
    File,
    Form
)

from fastapi.responses import HTMLResponse

from fastapi.staticfiles import StaticFiles

from fastapi.templating import Jinja2Templates

from .database import engine, Base

from .extractor import extract_text_from_pdf

from .ocr import extract_text_from_image

from .classifier import classify_document

from .processors.resume_processor import process_resume

from .processors.offer_letter_processor import (
    process_offer_letter
)

from .processors.invoice_processor import (
    process_invoice
)

from .processors.meeting_processor import (
    process_meeting_notes
)

import shutil
import os

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.mount(
    "/static",
    StaticFiles(directory="app/static"),
    name="static"
)

templates = Jinja2Templates(
    directory="app/templates"
)

UPLOAD_DIR = os.path.join(
    os.path.dirname(__file__),
    "uploads"
)

os.makedirs(
    UPLOAD_DIR,
    exist_ok=True
)

@app.get("/", response_class=HTMLResponse)

async def home(request: Request):

    return templates.TemplateResponse(
        request=request,
        name="index.html"
    )

@app.post("/upload")

async def upload_file(

    request: Request,

    file: UploadFile = File(None),

    meeting_text: str = Form("")

):

    text = ""

    # =========================
    # FILE PROCESSING
    # =========================

    if file and file.filename != "":

        filepath = os.path.join(
            UPLOAD_DIR,
            file.filename
        )

        with open(filepath, "wb") as buffer:

            shutil.copyfileobj(
                file.file,
                buffer
            )

        if file.filename.endswith(".pdf"):

            text = extract_text_from_pdf(
                filepath
            )

        elif (
            file.filename.endswith(".png")
            or file.filename.endswith(".jpg")
            or file.filename.endswith(".jpeg")
        ):

            text = extract_text_from_image(
                filepath
            )

    # =========================
    # TEXT INPUT PROCESSING
    # =========================

    elif meeting_text.strip() != "":

        text = meeting_text

    else:

        return {
            "error":
            "No file or text provided."
        }

    # =========================
    # DOCUMENT CLASSIFICATION
    # =========================

    document_type = classify_document(
        text
    )

    # =========================
    # PROCESSORS
    # =========================

    if document_type == "Resume":

        processed_data = process_resume(
            text
        )

    elif document_type == "Offer Letter":

        processed_data = process_offer_letter(
            text
        )

    elif document_type == "Invoice":

        processed_data = process_invoice(
            text
        )

    elif document_type == "Meeting Notes":

        processed_data = process_meeting_notes(
            text
        )

    else:

        processed_data = {

            "document_type":
            "General Document"

        }

    return processed_data