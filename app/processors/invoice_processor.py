import re

def process_invoice(text):

    invoice_number = re.search(
        r"invoice\s*no\.?\:?\s*([A-Z0-9#-]+)",
        text,
        re.IGNORECASE
    )

    amount = re.search(
        r"\$[\s]*([\d,]+\.\d+|\d+)",
        text
    )

    invoice_date = re.search(
        r"date\s*\:?\s*(\d{2}[./-]\d{2}[./-]\d{4})",
        text,
        re.IGNORECASE
    )

    due_date = re.search(
        r"due\s*date\s*\:?\s*(\d{2}[./-]\d{2}[./-]\d{4})",
        text,
        re.IGNORECASE
    )

    bank_name = re.search(
        r"([A-Za-z]+\sBank)",
        text,
        re.IGNORECASE
    )

    vendor = re.search(
        r"ISSUED TO:\s*([A-Za-z\s]+)",
        text,
        re.IGNORECASE
    )

    data = {

        "document_type": "Invoice",

        "vendor":
            (
                vendor.group(1).strip()
                if vendor else "Not Found"
            ),

        "invoice_number":
            (
                invoice_number.group(1)
                if invoice_number else "Not Found"
            ),

        "invoice_amount":
            (
                "$" + amount.group(1)
                if amount else "Not Found"
            ),

        "invoice_date":
            (
                invoice_date.group(1)
                if invoice_date else "Not Found"
            ),

        "due_date":
            (
                due_date.group(1)
                if due_date else "Not Found"
            ),

        "bank_name":
            (
                bank_name.group(1)
                if bank_name else "Not Found"
            ),

        "actions": [
            "Verify invoice details",
            "Approve payment",
            "Process vendor transaction"
        ]
    }

    return data