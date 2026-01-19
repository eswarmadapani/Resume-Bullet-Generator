# Service for calculating ATS (Applicant Tracking System) scores
def calculate_ats_score(keyword_match_percentage: float, resume_text: str) -> dict:
    score = 0
    breakdown = {}

    keyword_score = keyword_match_percentage * 0.6
    breakdown["keyword_match"] = round(keyword_score, 2)
    score += keyword_score

    word_count = len(resume_text.split())

    if word_count >= 300:
        length_score = 20
    elif word_count >= 200:
        length_score = 15
    elif word_count >= 100:
        length_score = 10
    else:
        length_score = 5

    breakdown["resume_length"] = length_score
    score += length_score

    final_score = min(round(score, 2), 100)

    return {
        "ats_score": final_score,
        "breakdown": breakdown
    }
