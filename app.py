import streamlit as st
import pdfplumber
from docx import Document
from PIL import Image
import pytesseract
from pdf2image import convert_from_bytes

from document_rules import detect_documents


st.set_page_config(
    page_title="Export Workflow Assistant",
    layout="wide"
)

st.title("📦 Export Workflow Assistant")

st.write(
    "Akreditif, PDF, Word veya görsel dosyalarını yükleyin."
)


def read_docx(file):

    doc = Document(file)

    text = []

    for paragraph in doc.paragraphs:
        text.append(paragraph.text)

    return "\n".join(text)


def read_pdf(file):

    extracted_text = ""

    try:

        with pdfplumber.open(file) as pdf:

            for page in pdf.pages:

                page_text = page.extract_text()

                if page_text:
                    extracted_text += page_text + "\n"

    except Exception:
        pass

    return extracted_text


def ocr_image(image):

    try:
        return pytesseract.image_to_string(image)

    except Exception as e:
        return f"OCR Hatası: {e}"


def ocr_pdf(file):

    text = ""

    try:

        images = convert_from_bytes(file.read())

        for img in images:

            text += pytesseract.image_to_string(img)

    except Exception:
        pass

    return text


uploaded_file = st.file_uploader(
    "Dosya Yükle",
    type=[
        "pdf",
        "docx",
        "jpg",
        "jpeg",
        "png"
    ]
)

if uploaded_file:

    file_name = uploaded_file.name.lower()

    extracted_text = ""

    if file_name.endswith(".docx"):

        extracted_text = read_docx(uploaded_file)

    elif file_name.endswith(".pdf"):

        extracted_text = read_pdf(uploaded_file)

        if len(extracted_text.strip()) < 50:

            uploaded_file.seek(0)

            extracted_text = ocr_pdf(uploaded_file)

    elif file_name.endswith(
        (
            ".jpg",
            ".jpeg",
            ".png"
        )
    ):

        image = Image.open(uploaded_file)

        extracted_text = ocr_image(image)

    st.subheader("Çıkarılan Metin")

    st.text_area(
        "",
        extracted_text,
        height=300
    )

    detected_docs = detect_documents(extracted_text)

    st.subheader("Tespit Edilen Belgeler")

    if detected_docs:

        for doc in detected_docs:

            st.success(doc)

    else:

        st.warning(
            "Herhangi bir belge tespit edilemedi."
        )
