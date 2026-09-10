import os
import shutil
import pytest

from app import process_pdf_upload, UPLOAD_DIR


def teardown_function(_):
    if os.path.exists(UPLOAD_DIR):
        shutil.rmtree(UPLOAD_DIR)


def test_process_pdf_upload_success():
    result = process_pdf_upload("report.pdf", b"%PDF-1.4 fake content")
    assert result["filename"] == "report.pdf"
    assert os.path.exists(result["path"])


def test_process_pdf_upload_rejects_non_pdf():
    with pytest.raises(ValueError):
        process_pdf_upload("report.txt", b"not a pdf")