# rules.py
DOCUMENT_RULES = {
    "Commercial Invoice": {
        "required_fields": ["Exporter", "Importer", "Invoice No", "HS Code", "Incoterm", "Total Amount"],
        "advice": "Fatura, akreditifteki mal tanımı ile %100 uyumlu olmalıdır. Fiyatlar akreditif tutarını aşmamalıdır."
    },
    "Bill of Lading": {
        "required_fields": ["Shipper", "Consignee", "Notify Party", "Port of Loading", "Port of Discharge", "Gross Weight"],
        "advice": "Konşimento 'Clean on Board' olmalı ve navlun ödemesi akreditif şartına uygun olmalıdır."
    },
    "Packing List": {
        "required_fields": ["Invoice Reference", "Package Count", "Net Weight", "Gross Weight"],
        "advice": "Paketleme listesindeki ağırlık ve miktar bilgileri fatura ile birebir örtüşmelidir."
    },
    "Certificate of Origin": {
        "required_fields": ["Exporter", "Importer", "Goods Description", "Origin Country"],
        "advice": "Menşe ülke faturadaki ile tutarlı olmalı, evrakta yetkili makamın mührü bulunmalıdır."
    },
    "Insurance Policy": {
        "required_fields": ["Policy Number", "Insured Amount", "Coverage Clauses"],
        "advice": "Sigorta poliçesi, akreditif tutarının en az %110'unu kapsamalıdır."
    }
}
