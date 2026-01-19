# Service for parsing job description files
import spacy
from typing import List

nlp = spacy.load("en_core_web_sm")

STOP_POS = {"DET", "PRON", "PUNCT", "SPACE", "SYM"}


def parse_job_description(jb_text: str) -> dict:
    if not jb_text or not jb_text.strip():
        raise ValueError("Job description text cannot be empty")
    
    doc = nlp(jb_text.lower())

    keywords = set()
    actions_verbs = set()
    
    for token in doc:
        if token.pos_ in STOP_POS:
            continue
        if token.pos_ == "NOUN" and len(token.text) > 2:
            keywords.add(token.lemma_)

        if token.pos_ == "VERB" and len(token.text) > 2:
            actions_verbs.add(token.lemma_)
    
    return {
        "keywords":sorted(list(keywords)),
        "action_verbs":sorted(list(actions_verbs))
    }