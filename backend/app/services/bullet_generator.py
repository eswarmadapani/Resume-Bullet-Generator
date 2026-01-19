import os
from dotenv import load_dotenv
from groq import Groq
from fastapi import HTTPException

# Load environment variables
load_dotenv()

# Initialize Groq client - will be checked at runtime
client = None
if os.getenv("GROQ_API_KEY"):
    client = Groq(api_key=os.getenv("GROQ_API_KEY"))

SYSTEM_PROMPT = """You are an ATS Resume Optimization Expert.

Your task is to rewrite weak or generic resume bullet points into strong, concise, ATS-friendly bullets aligned with a provided job description.
Rules:
Use clear action verbs (e.g., led, optimized, implemented, analyzed).
Integrate relevant keywords and skills from the job description naturally.
Do NOT invent metrics, numbers, titles, tools, or achievements that are not explicitly present.
Preserve the original meaning and scope of each bullet point.
Keep bullets concise, impact-focused, and professional (1 line each).
Avoid fluff, buzzwords without context, and first-person language.
Output Requirements:
Return only the rewritten bullet points
Do not include explanations, headings, commentary, or formatting outside of bullet points.
Process:
Analyze the original bullet point for intent and responsibilities.
Identify relevant ATS keywords from the job description.
Rewrite the bullet using strong verbs and optimized phrasing while remaining truthful.
Input You Will Receive:
Original resume bullet point(s)
Job description or target role (if provided)
Output Example:
Original: “Responsible for helping with reports”
Rewritten: “Prepared and maintained operational reports to support cross-functional decision-making"""

def generate_improved_bullets(weak_bullets:list, jd_keywords: list) -> list:
    if not weak_bullets:
        return []

    keywords = ",".join(jd_keywords[:8])

    user_prompt = f"""
You are provided with job description keywords and weak resume bullet points.

Job Description Keywords:
{keywords}

Weak Resume Bullet Points:
{chr(10).join(f"- {b}" for b in weak_bullets)}

Instructions:
- Rewrite EACH bullet point to be strong, concise, and ATS-friendly.
- Use clear action verbs and incorporate relevant job description keywords naturally.
- Do NOT add metrics, tools, achievements, or details that are not explicitly stated.
- Preserve the original meaning and responsibility of each bullet.
- Keep each rewritten bullet to one professional resume-ready line.

Output Requirements:
- Return ONLY the rewritten bullet points.
- Do NOT include explanations, headings, or extra formatting.
"""

    try:
        if not client:
            raise HTTPException(
                status_code=500,
                detail="GROQ_API_KEY environment variable not set"
            )
        
        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages = [
                {"role":"system","content":SYSTEM_PROMPT},
                {"role":"user","content":user_prompt}
            ],
            temperature=0.4
        )

        content = response.choices[0].message.content
        improved = [
            line.strip("- ").strip()
            for line in content.split("\n")
            if line.strip()
        ]

        return improved
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error generating improved bullets: {str(e)}")