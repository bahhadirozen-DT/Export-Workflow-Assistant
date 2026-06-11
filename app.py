import streamlit as st
import pandas as pd
from rules import DOCUMENT_RULES
from document_rules import detect_documents

# [Buraya diğer OCR/Dosya okuma fonksiyonlarını yine ekle]

st.title("🚢 Export Workflow Planner")

# Analiz Sekmesi
if st.button("Dokümanları Analiz Et ve Plan Oluştur"):
    # ... metin çıkarma ...
    detected = detect_documents(extracted_text)
    
    st.subheader("İhracat Operasyon Planı")
    for doc in detected:
        if doc in DOCUMENT_RULES:
            with st.expander(f"📌 {doc} Hazırlık Görevleri"):
                st.write(f"**Rehber:** {DOCUMENT_RULES[doc]['advice']}")
                # Burada Checklist oluşturuyoruz
                for field in DOCUMENT_RULES[doc]['required_fields']:
                    st.checkbox(f"Alan Kontrolü: {field}")
        else:
            st.error(f"{doc} için tanımlı kural yok!")
