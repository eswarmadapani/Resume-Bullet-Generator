# Service for parsing job description files
import re
from typing import List

# Common action verbs for resumes
COMMON_ACTION_VERBS = {
    "lead", "manage", "develop", "create", "implement", "design",
    "build", "improve", "optimize", "analyze", "collaborate", "coordinate",
    "execute", "deliver", "achieve", "increase", "reduce", "drive"
}

# Common stop words to filter out
STOP_WORDS = {
    "the", "a", "an", "and", "or", "but", "in", "on", "at", "to", "for",
    "of", "with", "by", "from", "as", "is", "was", "are", "were", "be",
    "been", "being", "have", "has", "had", "do", "does", "did", "will",
    "would", "should", "could", "may", "might", "must", "can", "about",
    "into", "through", "during", "before", "after", "above", "below",
    "between", "under", "over", "again", "further", "then", "once"
}

def parse_job_description(jb_text: str) -> dict:
    if not jb_text or not jb_text.strip():
        raise ValueError("Job description text cannot be empty")
    
    # Convert to lowercase and split into words
    text_lower = jb_text.lower()
    
    # Extract words (alphanumeric + hyphen)
    words = re.findall(r'\b[a-z][a-z0-9-]*\b', text_lower)
    
    keywords = set()
    action_verbs = set()
    
    for word in words:
        # Skip short words and stop words
        if len(word) <= 2 or word in STOP_WORDS:
            continue
            
        # Check if it's an action verb
        if word in COMMON_ACTION_VERBS:
            action_verbs.add(word)
        else:
            # Technical keywords, skills, tools
            keywords.add(word)
    
    return {
        "keywords": sorted(list(keywords))[:30],  # Limit to top 30
        "action_verbs": sorted(list(action_verbs))
    }