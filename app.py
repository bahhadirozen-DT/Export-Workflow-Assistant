import streamlit as st
import pdfplumber
from docx import Document
from PIL import Image
import pytesseract
from pdf2image import convert_from_bytes
from document_rules import detect_documents
from rules import DOCUMENT_RULES  # rules.py dosyanın olduğundan emin ol

st.set_page_config(page_title="Export Workflow Assistant", layout="wide")

st.title("📦 Export Workflow Assistant")
st.write("Akreditif, PDF, Word veya görsel dosyalarını yükleyin, operasyon planınızı alın.")

# --- Fonksiyonlar ---
def read_docx(file):
    doc = Document(file)
    return "\n".join([p.text for p in doc.paragraphs])

def read_pdf(file):
    text = ""
    try:
        with pdfplumber.open(file) as pdf:
            for page in pdf.pages:
                t = page.extract_text()
                if t: text += t + "\n"
    except: pass
    return text

def ocr_image(image):
    try: return pytesseract.image_to_string(image)
    except: return "OCR Hatası oluştu."

def ocr_pdf(file):
    text = ""
    try:
        images = convert_from_bytes(file.read())
        for img in images: text += pytesseract.image_to_string(img)
    except: pass
    return text

# --- Arayüz ---
uploaded_file = st.file_uploader("Dosya Yükle", type=["pdf", "docx", "jpg", "jpeg", "png"])

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
    elif file_name.endswith((".jpg", ".jpeg", ".png")):
        image = Image.open(uploaded_file)
        extracted_text = ocr_image(image)

    st.subheader("Çıkarılan Metin")
    st.text_area("", extracted_text, height=200)

    # --- Operasyonel Planlayıcı ---
    detected_docs = detect_documents(extracted_text)
    st.subheader("Operasyon Rehberi ve Checklist")

    if detected_docs:
        for doc in detected_docs:
            with st.expander(f"✅ {doc} - Hazırlık Planı", expanded=True):
                if doc in DOCUMENT_RULES:
                    rule = DOCUMENT_RULES[doc]
                    st.markdown(f"**💡 Tavsiye:** {rule['advice']}")
                    st.markdown("**📋 Doldurulması Gerekenler:**")
                    for field in rule['required_fields']:
                        st.checkbox(f"{field}")
                else:
                    st.info("Bu belge için sistemde kural tanımlı değil.")
    else:
        st.warning("Belge tespit edilemedi.")
