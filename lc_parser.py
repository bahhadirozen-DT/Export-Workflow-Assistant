import re

def parse_lc_text(text):
    # 46A alanını yakalayan regex
    pattern_46a = r"46A:(.*?)(?=47A:|44A:|44B:|44C:|50:|59:|71B:|$)"
    match = re.search(pattern_46a, text, re.DOTALL | re.IGNORECASE)
    
    if match:
        content = match.group(1).strip()
        # Satırlara böl ve listele
        documents = [line.strip() for line in content.split('\n') if line.strip()]
        return documents
    return []
