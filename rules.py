# rules.py

DOCUMENT_RULES = {
    "Commercial Invoice": {
        "required_fields": ["Exporter", "Importer", "Invoice No", "HS Code", "Incoterm"],
        "advice": "Fatura, akreditifteki mal tanımı ile %100 uyumlu olmalıdır. Fiyatlar akreditif tutarını aşmamalıdır."
    },
    "Bill of Lading": {
        "required_fields": ["Shipper", "Consignee", "Notify Party", "Port of Loading", "Gross Weight"],
        "advice": "Konşimento 'Clean on Board' olmalı ve navlun ödemesi akreditifteki 'Freight Prepaid/Collect' şartına uygun olmalıdır."
    },
    "Certificate of Origin": {
        "required_fields": ["Exporter", "Importer", "Origin Country"],
        "advice": "Menşe ülke, faturadaki menşe ile tutarlı olmalı ve ticaret odası onayı unutulmamalıdır."
    }
}
