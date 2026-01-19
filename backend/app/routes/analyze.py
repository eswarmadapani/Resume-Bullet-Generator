from fastapi import APIRouter, UploadFile, File, Form
from app.services.resume_parser import parse_resume
from app.services.jd_parser import parse_job_description
from app.utils.keyword_matcher import match_keywords
from app.services.ats_scoring import calculate_ats_score
from app.utils.text_cleaner import clean_text
from app.services.bullet_analyzer import analyze_bullets
from app.services.bullet_generator import generate_improved_bullets

router = APIRouter()

@router.post("/analyze")
async def analyze_resume(
    resume: UploadFile = File(...),
    job_description: str = Form(...)
):
    raw_resume_text = parse_resume(resume)
    clean_resume_text = clean_text(raw_resume_text)

    clean_jd_text = clean_text(job_description)
    jd_data = parse_job_description(clean_jd_text)

    keyword_match = match_keywords(
        resume_text=clean_resume_text,
        jd_keywords=jd_data["keywords"]
    )

    ats_result = calculate_ats_score(
        keyword_match_percentage=keyword_match["matched_percentage"],
        resume_text=clean_resume_text
    )

    bullet_analysis = analyze_bullets(raw_resume_text)

    improved_bullets = generate_improved_bullets(
        weak_bullets=bullet_analysis["weak_bullets"],
        jd_keywords=jd_data["keywords"]
    )

    return {
        "ats_score": ats_result["ats_score"],
        "score_breakdown": ats_result["breakdown"],
        "matched_keywords": keyword_match["matched_keywords"][:15],
        "missing_keywords": keyword_match["missing_keywords"][:15],
        "weak_bullets": bullet_analysis["weak_bullets"],
        "improved_bullets": improved_bullets
    }
