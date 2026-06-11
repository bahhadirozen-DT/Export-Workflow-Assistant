# rules.py
DOCUMENT_RULES = {
    "Commercial Invoice": {
        "required_fields": ["Exporter", "Importer", "Invoice No", "HS Code", "Incoterm", "Total Amount"],
        "advice": "Fatura, akreditifteki mal tanımı ile %100 uyumlu olmalıdır.",
        "critical_check": "Fatura tutarı, akreditif tutarını aşmamalıdır."
    },
    "Bill of Lading": {
        "required_fields": ["Shipper", "Consignee", "Notify Party", "Port of Loading", "Port of Discharge", "Gross Weight"],
        "advice": "Konşimento 'Clean on Board' olmalı ve navlun ödemesi akreditif şartına uygun olmalıdır.",
        "critical_check": "Notify Party kısmının LC'deki madde ile birebir aynı olduğundan emin olun."
    },
    "Packing List": {
        "required_fields": ["Invoice Reference", "Package Count", "Net Weight", "Gross Weight"],
        "advice": "Paketleme listesindeki toplam ağırlık, fatura ve konşimento ile tutarlı olmalıdır.",
        "critical_check": "Paketleme detayları (koli adedi/tipi) akreditif ile çelişmemelidir."
    },
    "Certificate of Origin": {
        "required_fields": ["Exporter", "Importer", "Goods Description", "Origin Country"],
        "advice": "Menşe ülke faturadaki ile tutarlı olmalı, evrakta yetkili makamın mührü bulunmalıdır.",
        "critical_check": "Ticaret Odası onayı veya tasdik tarihinin güncel olduğunu kontrol edin."
    },
    "Insurance Policy": {
        "required_fields": ["Policy Number", "Insured Amount", "Coverage Clauses"],
        "advice": "Sigorta poliçesi, akreditif tutarının en az %110'unu kapsamalıdır.",
        "critical_check": "Sigorta başlangıç tarihi, yükleme tarihinden önce veya aynı gün olmalıdır."
    }
}
