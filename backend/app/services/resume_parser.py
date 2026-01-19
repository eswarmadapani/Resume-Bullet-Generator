# Service for parsing resume files (PDF, DOCX)
import pdfplumber 
from docx import Document
from fastapi import UploadFile,HTTPException

ALLOWED_EXTENSIONS = {"pdf", "docx"}


def get_file_extension(filename: str):
    return filename.split(".")[-1].lower()


def parse_resume(file: UploadFile) -> str:
    extension = get_file_extension(file.filename)

    if extension not in ALLOWED_EXTENSIONS:
        raise HTTPException(status_code=400, detail="Invalid file type")
    
    if extension == "pdf":
        return extract_text_from_pdf(file)

    elif extension == "docx":
        return extract_text_from_docx(file)

def extract_text_from_pdf(file: UploadFile) -> str:
    text = ""

    try:
        with pdfplumber.open(file.file) as pdf:
            for page in pdf.pages:
                page_text = page.extract_text()
                if page_text:
                    text += page_text + "\n"
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error parsing PDF: {str(e)}")
    
    if not text.strip():
        raise HTTPException(status_code=400, detail="PDF is empty or unreadable")
    
    return text.strip()
    

def extract_text_from_docx(file: UploadFile) -> str:
    try:
        document = Document(file.file)
        text = "\n".join([para.text for para in document.paragraphs])
    except Exception:
        raise HTTPException(status_code=500, detail="Failed to read DOCX file")

    if not text.strip():
        raise HTTPException(
            status_code=422,
            detail="No readable text found in DOCX file"
        )

    return text.strip()