import spacy
from collections import Counter
import string

def load_file(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        return file.read().lower()

def clean_text(text):
    return text.translate(str.maketrans('', '', string.punctuation))

def extract_keywords(text, nlp):
    doc = nlp(text)
    keywords = [token.text for token in doc if token.is_alpha and not token.is_stop]
    return Counter(keywords)

def compare_keywords(resume_words, job_words):
    common = set(resume_words) & set(job_words)
    score = len(common) / len(job_words) * 100  # simple similarity score
    return score, common

def main():
    nlp = spacy.load("en_core_web_sm")

    resume_text = clean_text(load_file("resume.txt"))
    job_text = clean_text(load_file("job_description.txt"))

    resume_keywords = extract_keywords(resume_text, nlp)
    job_keywords = extract_keywords(job_text, nlp)

    score, common_keywords = compare_keywords(resume_keywords, job_keywords)

    print(f"\nMatch Score: {score:.2f}/100")
    print("Matching Keywords:", ", ".join(common_keywords))

    missing = set(job_keywords) - set(resume_keywords)
    print("Suggested skills to add:", ", ".join(missing))

if __name__ == "__main__":
    main()

