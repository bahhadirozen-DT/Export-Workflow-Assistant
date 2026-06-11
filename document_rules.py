DOCUMENT_RULES = {
    "Commercial Invoice": [
        "commercial invoice",
        "signed commercial invoice",
        "invoice"
    ],

    "Packing List": [
        "packing list"
    ],

    "Bill of Lading": [
        "bill of lading",
        "full set clean on board",
        "b/l",
        "ocean bill of lading"
    ],

    "Certificate of Origin": [
        "certificate of origin",
        "origin certificate"
    ],

    "Insurance Policy": [
        "insurance policy",
        "insurance certificate"
    ],

    "Inspection Certificate": [
        "inspection certificate"
    ],

    "Beneficiary Certificate": [
        "beneficiary certificate"
    ]
}


def detect_documents(text: str):

    found_documents = []

    text = text.lower()

    for document_name, keywords in DOCUMENT_RULES.items():

        for keyword in keywords:

            if keyword in text:
                found_documents.append(document_name)
                break

    return sorted(list(set(found_documents)))DOCUMENT_RULES = {
    "Commercial Invoice": [
        "commercial invoice",
        "signed commercial invoice",
        "invoice"
    ],

    "Packing List": [
        "packing list"
    ],

    "Bill of Lading": [
        "bill of lading",
        "full set clean on board",
        "b/l",
        "ocean bill of lading"
    ],

    "Certificate of Origin": [
        "certificate of origin",
        "origin certificate"
    ],

    "Insurance Policy": [
        "insurance policy",
        "insurance certificate"
    ],

    "Inspection Certificate": [
        "inspection certificate"
    ],

    "Beneficiary Certificate": [
        "beneficiary certificate"
    ]
}


def detect_documents(text: str):

    found_documents = []

    text = text.lower()

    for document_name, keywords in DOCUMENT_RULES.items():

        for keyword in keywords:

            if keyword in text:
                found_documents.append(document_name)
                break

    return sorted(list(set(found_documents)))DOCUMENT_RULES = {
    "Commercial Invoice": [
        "commercial invoice",
        "signed commercial invoice",
        "invoice"
    ],

    "Packing List": [
        "packing list"
    ],

    "Bill of Lading": [
        "bill of lading",
        "full set clean on board",
        "b/l",
        "ocean bill of lading"
    ],

    "Certificate of Origin": [
        "certificate of origin",
        "origin certificate"
    ],

    "Insurance Policy": [
        "insurance policy",
        "insurance certificate"
    ],

    "Inspection Certificate": [
        "inspection certificate"
    ],

    "Beneficiary Certificate": [
        "beneficiary certificate"
    ]
}


def detect_documents(text: str):

    found_documents = []

    text = text.lower()

    for document_name, keywords in DOCUMENT_RULES.items():

        for keyword in keywords:

            if keyword in text:
                found_documents.append(document_name)
                break

    return sorted(list(set(found_documents)))DOCUMENT_RULES = {
    "Commercial Invoice": [
        "commercial invoice",
        "signed commercial invoice",
        "invoice"
    ],

    "Packing List": [
        "packing list"
    ],

    "Bill of Lading": [
        "bill of lading",
        "full set clean on board",
        "b/l",
        "ocean bill of lading"
    ],

    "Certificate of Origin": [
        "certificate of origin",
        "origin certificate"
    ],

    "Insurance Policy": [
        "insurance policy",
        "insurance certificate"
    ],

    "Inspection Certificate": [
        "inspection certificate"
    ],

    "Beneficiary Certificate": [
        "beneficiary certificate"
    ]
}


def detect_documents(text: str):

    found_documents = []

    text = text.lower()

    for document_name, keywords in DOCUMENT_RULES.items():

        for keyword in keywords:

            if keyword in text:
                found_documents.append(document_name)
                break

    return sorted(list(set(found_documents)))
