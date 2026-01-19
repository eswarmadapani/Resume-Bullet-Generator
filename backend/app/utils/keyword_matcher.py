from typing import Dict, List

def match_keywords(resume_text: str, jd_keywords: List) -> Dict:
    resume_text = resume_text.lower()

    matched = []
    missing = []

    for keyword in jd_keywords:
        if keyword in resume_text:
            matched.append(keyword)
        else:
            missing.append(keyword)
    
    total = len(jd_keywords)
    matched_percent =  round((len(matched) / total) * 100, 2) if total > 0 else 0
    return{
        "matched_keywords":matched,
        "missing_keywords":missing,
        "matched_percentage":matched_percent
    }