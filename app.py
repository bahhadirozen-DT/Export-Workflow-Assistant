import streamlit as st
import pandas as pd
import os
from docx import Document
import pdfplumber
from PIL import Image
import pytesseract
from pdf2image import convert_from_bytes
from document_rules import detect_documents
from rules import DOCUMENT_RULES

# Uploads klasörünü oluştur
if not os.path.exists("uploads"):
    os.makedirs("uploads")

st.set_page_config(page_title="Export Workflow Assistant", layout="wide")

st.title("📦 Export Workflow Assistant")

# Sekmeler
tab1, tab2 = st.tabs(["🚀 Operasyon İşlemleri", "📊 Analiz ve Dosya Yönetimi"])

if 'analysis_history' not in st.session_state:
    st.session_state.analysis_history = []

# Fonksiyonlar
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
    except: return "OCR Hatası."

def ocr_pdf(file):
    text = ""
    try:
        images = convert_from_bytes(file.read())
        for img in images: text += pytesseract.image_to_string(img)
    except: pass
    return text

with tab1:
    uploaded_file = st.file_uploader("Dosya Yükle", type=["pdf", "docx", "jpg", "jpeg", "png"])
    
    if uploaded_file:
        # Fiziksel kaydet
        file_path = os.path.join("uploads", uploaded_file.name)
        with open(file_path, "wb") as f:
            f.write(uploaded_file.getbuffer())

        # Metni al
        file_name = uploaded_file.name.lower()
        extracted_text = ""
        if file_name.endswith(".docx"): extracted_text = read_docx(uploaded_file)
        elif file_name.endswith(".pdf"):
            extracted_text = read_pdf(uploaded_file)
            if len(extracted_text.strip()) < 50:
                uploaded_file.seek(0)
                extracted_text = ocr_pdf(uploaded_file)
        elif file_name.endswith((".jpg", ".jpeg", ".png")):
            image = Image.open(uploaded_file)
            extracted_text = ocr_image(image)

        detected_docs = detect_documents(extracted_text)
        
        if not any(d['Dosya'] == uploaded_file.name for d in st.session_state.analysis_history):
            st.session_state.analysis_history.append({"Dosya": uploaded_file.name, "Tespit Edilenler": ", ".join(detected_docs)})

        for doc in detected_docs:
            with st.expander(f"✅ {doc} - Hazırlık Planı", expanded=True):
                if doc in DOCUMENT_RULES:
                    rule = DOCUMENT_RULES[doc]
                    st.markdown(f"**💡 Tavsiye:** {rule['advice']}")
                    st.error(f"⚠️ **Kritik Kontrol:** {rule['critical_check']}")
                    for field in rule['required_fields']:
                        st.checkbox(f"{field} hazır")
                else:
                    st.info("Bu belge için özel kural tanımlı değil.")

with tab2:
    st.header("Dosya Deposu ve Analiz Geçmişi")
    # Dosya deposunu göster
    files = os.listdir("uploads")
    st.write("### Yüklenen Dosyalar:", files)
    
    if st.session_state.analysis_history:
        df = pd.DataFrame(st.session_state.analysis_history)
        st.table(df)
        if st.button("Analiz Raporunu İndir (Excel)"):
            df.to_excel("operasyon_raporu.xlsx", index=False)
            st.success("operasyon_raporu.xlsx oluşturuldu!")
    else:
        st.info("Henüz analiz edilen dosya yok.")
