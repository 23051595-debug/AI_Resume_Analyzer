import streamlit as st
import pdfplumber
import re
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from sklearn.metrics.pairwise import cosine_similarity
from sentence_transformers import SentenceTransformer
import random


model = SentenceTransformer('all-MiniLM-L6-v2')


nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')


st.set_page_config(page_title="AI Resume Analyzer", layout="centered")
st.title("AI Resume Analyzer & Job Matcher")
st.write("Upload your resume and paste job description to get matching score & missing skills.")


resume_file = st.file_uploader("Upload Resume (PDF)", type=["pdf"])
job_description = st.text_area("Paste Job Description here")



def extract_text_from_pdf(uploaded_file):
    text = ""
    with pdfplumber.open(uploaded_file) as pdf:
        for page in pdf.pages:
            if page.extract_text():
                text += page.extract_text() + "\n"
    return text


def clean_text(text):
    text = text.lower()
    text = re.sub(r'[^a-z\s]', '', text)
    tokens = word_tokenize(text)
    stop_words = set(stopwords.words('english'))
    tokens = [w for w in tokens if w not in stop_words]
    lemmatizer = WordNetLemmatizer()
    tokens = [lemmatizer.lemmatize(w) for w in tokens]
    return " ".join(tokens)


def semantic_similarity_score(text1, text2):
    embeddings = model.encode([text1, text2])
    similarity = cosine_similarity([embeddings[0]], [embeddings[1]])
    return round(similarity[0][0] * 100, 2)


SKILLS_DB = [
    "python","java","c++","machine learning","deep learning","data science","nlp",
    "sql","mysql","mongodb","html","css","javascript","react","node","django",
    "flask","aws","docker","kubernetes","git","github","linux","tensorflow",
    "pytorch","opencv"
]


def extract_skills(text):
    tokens = word_tokenize(text)
    bigrams = [" ".join(tokens[i:i+2]) for i in range(len(tokens)-1)]
    trigrams = [" ".join(tokens[i:i+3]) for i in range(len(tokens)-2)]
    all_phrases = tokens + bigrams + trigrams

    extracted = []
    for skill in SKILLS_DB:
        for phrase in all_phrases:
            if skill == phrase:
                extracted.append(skill)

    return list(set(extracted))


def find_missing_skills(resume_text, job_text):
    resume_skills = extract_skills(resume_text)
    job_skills = extract_skills(job_text)
    missing = list(set(job_skills) - set(resume_skills))
    return resume_skills, job_skills, missing


def generate_resume_feedback(missing_skills, semantic_score):
    suggestions = []

    if semantic_score < 40:
        suggestions.append("Your resume content is weakly aligned with the job description. Try rewriting your summary and project descriptions using relevant keywords.")
    elif semantic_score < 60:
        suggestions.append("Your resume partially matches the job description. Add more role-specific terminology and project details.")
    else:
        suggestions.append("Good resume relevance. Focus on improving skill coverage for better results.")

    for skill in missing_skills:
        suggestions.append(f"Consider learning and adding projects using {skill.upper()} to strengthen your profile.")

    if len(missing_skills) >= 4:
        suggestions.append("Your resume lacks several important technical skills. Consider doing 2–3 guided projects to improve employability.")

    if not missing_skills:
        suggestions.append("Excellent skill match. Focus on improving project impact statements and measurable achievements.")

    return suggestions


def rewrite_resume_bullet(bullet):
    action_verbs = [
        "Developed","Designed","Implemented","Optimized","Engineered",
        "Automated","Built","Created","Improved","Deployed"
    ]

    bullet = bullet.strip().lower()
    if len(bullet.split()) < 4:
        return "Please enter a more detailed bullet point for better rewriting."

    verb = random.choice(action_verbs)
    rewritten = f"{verb} {bullet}, enhancing performance, scalability, and maintainability."
    return rewritten.capitalize()



if st.button("Analyze Resume", key="analyze"):

    if resume_file and job_description.strip():

        with st.spinner("Analyzing..."):
            resume_text = extract_text_from_pdf(resume_file)
            clean_resume = clean_text(resume_text)
            clean_job = clean_text(job_description)

            resume_skills, job_skills, missing_skills = find_missing_skills(clean_resume, clean_job)

            semantic_score = semantic_similarity_score(clean_resume, clean_job)

            if len(job_skills) == 0:
                skill_score = 0
            else:
                matched_skills = set(resume_skills).intersection(set(job_skills))
                skill_score = (len(matched_skills) / len(job_skills)) * 100

            final_score = round((0.6 * semantic_score) + (0.4 * skill_score), 2)
            feedback = generate_resume_feedback(missing_skills, semantic_score)

        st.success("Analysis Completed!")

        st.subheader("Matching Score")
        st.metric("Resume Match", f"{final_score}%")

        st.subheader("Extracted Resume Skills")
        st.write(", ".join(resume_skills) if resume_skills else "No skills detected")

        st.subheader("Required Job Skills")
        st.write(", ".join(job_skills) if job_skills else "No skills detected")

        st.subheader("Missing Skills")
        if missing_skills:
            st.warning(", ".join(missing_skills))
        else:
            st.success("Great! No major skills missing 🎯")

        st.subheader("AI Resume Improvement Suggestions")
        for tip in feedback:
            st.info("💡 " + tip)

    else:
        st.error("Please upload resume and enter job description.")



st.divider()
st.subheader("🎯 AI Resume Bullet Rewriting Tool")

user_bullet = st.text_area("Paste a resume bullet point you want to improve")

if st.button("Rewrite Bullet", key="rewrite"):
    if user_bullet.strip():
        improved = rewrite_resume_bullet(user_bullet)
        st.success("Improved Resume Bullet:")
        st.write("👉 " + improved)
    else:
        st.error("Please enter a bullet point.")