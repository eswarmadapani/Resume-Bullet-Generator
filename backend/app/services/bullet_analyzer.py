# Service for analyzing resume bullet points
WEAK_VERBS = {
    "worked",
    "helped",
    "assisted",
    "responsible",
    "involved",
    "participated",
    "supported"
}

def analyze_bullets(resume_text: str) -> dict:
    lines = resume_text.split("\n")

    bullets = []
    weak_bullets = []

    for line in lines:
        line = line.strip()

        if len(line) < 10:
            continue

        if line.startswith(("-", "•", "*")):
            bullet = line.lstrip("-•* ").strip()
            bullets.append(bullet)

    for bullet in bullets:
        words = bullet.lower().split()

        if not words:
            continue

        first_word = words[0]

        if first_word in WEAK_VERBS or len(words) < 8:
            weak_bullets.append(bullet)

    return {
        "total_bullets": len(bullets),
        "weak_bullets": weak_bullets
    }
