# Export-Workflow-Assistant

Akreditif (Letter of Credit - LC) ve dış ticaret evraklarını analiz ederek gerekli belge listesini çıkaran operasyon destek sistemi.

## Mevcut Özellikler

* PDF okuma
* DOCX okuma
* OCR (JPG / JPEG / PNG)
* LC metin çıkarma
* Belge tespiti
* Temel checklist oluşturma

## Desteklenen Dosya Türleri

* PDF
* DOCX
* JPG
* JPEG
* PNG

## Amaç

Bir akreditif metni veya görseli yüklendiğinde:

* Commercial Invoice
* Packing List
* Bill of Lading
* Certificate of Origin
* Insurance Policy

gibi gerekli belgeleri otomatik olarak tespit etmek.

## Yol Haritası

### V1

* Dosya yükleme
* OCR
* Belge tespiti

### V2

* MT700 alan ayrıştırma
* 40A, 46A, 47A analizi

### V3

* Operasyon checklist üretimi

### V4

* Evrak şablonları oluşturma

### V5

* Yapay zekâ destekli operasyon planlama

## Kurulum

```bash
pip install -r requirements.txt
streamlit run app.py
```

## Örnek

Girdi:

```text
46A:

Signed Commercial Invoice
Packing List
Full Set Clean On Board Bill of Lading
Certificate of Origin
```

Çıktı:

```text
Commercial Invoice
Packing List
Bill of Lading
Certificate of Origin
```
