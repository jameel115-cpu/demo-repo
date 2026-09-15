import os

from database import log_upload

UPLOAD_DIR = "uploads"


def process_pdf_upload(filename: str, content: bytes) -> dict:
    """
    Saves an uploaded PDF file to disk and logs it in the database.
    Raises ValueError if the file is not a PDF.
    """
    if not filename.endswith(".pdf"):
        raise ValueError("Only PDF files are allowed.")

    file_path = os.path.join(UPLOAD_DIR, filename)

    with open(file_path, "wb") as f:
        f.write(content)

    record = {
        "filename": filename,
        "path": file_path,
        "size": len(content),
    }
    log_upload(record)
    return record
