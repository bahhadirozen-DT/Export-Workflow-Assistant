import os
from document_rules import detect_documents

# En son yüklenen dosyayı bul
files = [os.path.join("uploads", f) for f in os.listdir("uploads")]
latest_file = max(files, key=os.path.getctime)

# Basit analiz
with open(latest_file, 'rb') as f:
    text = "Küşat metni analiz ediliyor..." # Buraya PDF/OCR okuma fonksiyonunu ekleyebilirsin
    docs = detect_documents(text)
    
print(f"Analiz Tamamlandı: {docs}")
# Bu çıktı GitHub Actions loglarında görünecek!
