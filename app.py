import streamlit as st
import re
import math
from collections import Counter

from pypdf import PdfReader
from docx import Document


# =========================================================
# PAGE CONFIGURATION
# =========================================================

st.set_page_config(
    page_title="AI Job Recommendation System",
    page_icon="💼",
    layout="wide"
)


# =========================================================
# TITLE
# =========================================================

st.title("💼 AI Job Recommendation System")

st.write(
    "Upload your resume and our AI-based recommendation engine "
    "will analyze your skills and recommend suitable jobs."
)

st.divider()


# =========================================================
# JOB DATA
# =========================================================

jobs = [
    {
        "title": "Python Developer",
        "company": "Tech Solutions",
        "skills": ["python", "sql", "django", "apis"],
        "location": "Hyderabad",
        "description":
            "Develop Python applications and backend APIs using Python, SQL and Django."
    },

    {
        "title": "Web Developer",
        "company": "WebTech Solutions",
        "skills": ["html", "css", "javascript", "react"],
        "location": "Hyderabad",
        "description":
            "Build responsive websites using HTML, CSS, JavaScript and React."
    },

    {
        "title": "Data Analyst",
        "company": "Data Insights",
        "skills": ["python", "sql", "excel", "pandas"],
        "location": "Hyderabad",
        "description":
            "Analyze business data using Python, SQL, Excel and Pandas."
    },

    {
        "title": "Machine Learning Engineer",
        "company": "AI Labs",
        "skills": [
            "python",
            "machine learning",
            "scikit learn",
            "nlp"
        ],
        "location": "Bangalore",
        "description":
            "Develop machine learning models and artificial intelligence applications."
    },

    {
        "title": "Software Developer",
        "company": "Tech Innovations",
        "skills": [
            "java",
            "python",
            "sql",
            "data structures"
        ],
        "location": "Hyderabad",
        "description":
            "Develop and maintain software applications using Java and Python."
    },

    {
        "title": "Frontend Developer",
        "company": "Creative Tech",
        "skills": [
            "html",
            "css",
            "javascript",
            "react"
        ],
        "location": "Bangalore",
        "description":
            "Design and develop modern user-friendly web interfaces."
    },

    {
        "title": "Backend Developer",
        "company": "Code Works",
        "skills": [
            "python",
            "sql",
            "apis",
            "flask"
        ],
        "location": "Hyderabad",
        "description":
            "Develop server-side applications and APIs using Python and Flask."
    },

    {
        "title": "Data Scientist",
        "company": "Data Science Hub",
        "skills": [
            "python",
            "machine learning",
            "sql",
            "pandas"
        ],
        "location": "Bangalore",
        "description":
            "Build data science and machine learning solutions using Python."
    },

    {
        "title": "Java Developer",
        "company": "Enterprise Tech",
        "skills": [
            "java",
            "sql",
            "spring boot"
        ],
        "location": "Hyderabad",
        "description":
            "Develop enterprise applications using Java, SQL and Spring Boot."
    },

    {
        "title": "AI Engineer",
        "company": "Future AI",
        "skills": [
            "python",
            "machine learning",
            "nlp",
            "artificial intelligence"
        ],
        "location": "Bangalore",
        "description":
            "Develop artificial intelligence and NLP applications using Python."
    }
]


# =========================================================
# PDF TEXT EXTRACTION
# =========================================================

def extract_pdf_text(file):

    reader = PdfReader(file)

    text = ""

    for page in reader.pages:

        page_text = page.extract_text()

        if page_text:
            text += page_text + " "

    return text


# =========================================================
# DOCX TEXT EXTRACTION
# =========================================================

def extract_docx_text(file):

    document = Document(file)

    text = ""

    for paragraph in document.paragraphs:

        text += paragraph.text + " "

    return text


# =========================================================
# TEXT CLEANING
# =========================================================

def clean_text(text):

    text = text.lower()

    text = re.sub(
        r"[^a-z0-9\s]",
        " ",
        text
    )

    text = re.sub(
        r"\s+",
        " ",
        text
    )

    return text.strip()


# =========================================================
# TOKENIZATION
# =========================================================

def tokenize(text):

    text = clean_text(text)

    return text.split()


# =========================================================
# TF-IDF CALCULATION
# =========================================================

def calculate_tfidf(documents):

    tokenized_documents = [
        tokenize(doc)
        for doc in documents
    ]

    total_documents = len(tokenized_documents)

    # Document frequency
    document_frequency = Counter()

    for tokens in tokenized_documents:

        unique_words = set(tokens)

        for word in unique_words:
            document_frequency[word] += 1

    tfidf_documents = []

    for tokens in tokenized_documents:

        word_count = Counter(tokens)

        total_words = len(tokens)

        tfidf = {}

        if total_words == 0:
            tfidf_documents.append(tfidf)
            continue

        for word, count in word_count.items():

            tf = count / total_words

            df = document_frequency[word]

            idf = math.log(
                (total_documents + 1) /
                (df + 1)
            ) + 1

            tfidf[word] = tf * idf

        tfidf_documents.append(tfidf)

    return tfidf_documents


# =========================================================
# COSINE SIMILARITY
# =========================================================

def cosine_similarity(vector_a, vector_b):

    common_words = set(vector_a.keys()) & set(vector_b.keys())

    dot_product = sum(
        vector_a[word] * vector_b[word]
        for word in common_words
    )

    magnitude_a = math.sqrt(
        sum(value * value for value in vector_a.values())
    )

    magnitude_b = math.sqrt(
        sum(value * value for value in vector_b.values())
    )

    if magnitude_a == 0 or magnitude_b == 0:

        return 0

    return dot_product / (
        magnitude_a * magnitude_b
    )


# =========================================================
# SKILL DETECTION
# =========================================================

def find_skills(resume_text):

    all_skills = [
        "python",
        "java",
        "c",
        "c++",
        "html",
        "css",
        "javascript",
        "react",
        "sql",
        "mysql",
        "django",
        "flask",
        "machine learning",
        "deep learning",
        "artificial intelligence",
        "nlp",
        "pandas",
        "numpy",
        "scikit learn",
        "data science",
        "excel",
        "data structures",
        "spring boot",
        "apis"
    ]

    resume_lower = resume_text.lower()

    detected = []

    for skill in all_skills:

        if skill in resume_lower:

            detected.append(skill)

    return detected


# =========================================================
# SKILL MATCH SCORE
# =========================================================

def calculate_skill_score(resume_skills, job_skills):

    if not job_skills:

        return 0

    matched_skills = set(resume_skills) & set(job_skills)

    score = (
        len(matched_skills) /
        len(set(job_skills))
    ) * 100

    return score


# =========================================================
# RESUME UPLOAD
# =========================================================

resume = st.file_uploader(
    "📄 Upload your Resume",
    type=["pdf", "docx"]
)


# =========================================================
# MAIN PROCESS
# =========================================================

if resume:

    st.success("Resume uploaded successfully! ✅")

    # -----------------------------------------------------
    # EXTRACT TEXT
    # -----------------------------------------------------

    try:

        if resume.name.lower().endswith(".pdf"):

            resume_text = extract_pdf_text(resume)

        else:

            resume_text = extract_docx_text(resume)

    except Exception as error:

        st.error(
            f"Could not read the resume: {error}"
        )

        st.stop()


    # -----------------------------------------------------
    # CHECK TEXT
    # -----------------------------------------------------

    if not resume_text.strip():

        st.error(
            "No readable text was found in the resume."
        )

        st.info(
            "If your PDF is a scanned image, "
            "upload a text-based PDF or DOCX file."
        )

        st.stop()


    # -----------------------------------------------------
    # RESUME TEXT
    # -----------------------------------------------------

    with st.expander("📋 View Extracted Resume Text"):

        st.write(resume_text)


    # -----------------------------------------------------
    # DETECT SKILLS
    # -----------------------------------------------------

    resume_skills = find_skills(resume_text)


    st.subheader("🛠️ Skills Detected From Resume")

    if resume_skills:

        skill_text = " • ".join(
            skill.title()
            for skill in resume_skills
        )

        st.success(skill_text)

    else:

        st.warning(
            "No predefined technical skills were detected."
        )


    # -----------------------------------------------------
    # AI ANALYSIS
    # -----------------------------------------------------

    st.divider()

    st.subheader("🤖 AI Resume Analysis")

    st.write(
        "The system is comparing your resume with available "
        "job descriptions using TF-IDF and Cosine Similarity."
    )


    # -----------------------------------------------------
    # CREATE JOB DOCUMENTS
    # -----------------------------------------------------

    job_documents = []

    for job in jobs:

        job_text = (
            job["title"] + " " +
            " ".join(job["skills"]) + " " +
            job["description"]
        )

        job_documents.append(job_text)


    # -----------------------------------------------------
    # TF-IDF
    # -----------------------------------------------------

    all_documents = [resume_text] + job_documents

    tfidf_documents = calculate_tfidf(
        all_documents
    )

    resume_vector = tfidf_documents[0]


    # -----------------------------------------------------
    # CALCULATE JOB SCORES
    # -----------------------------------------------------

    recommendations = []

    for i, job in enumerate(jobs):

        job_vector = tfidf_documents[i + 1]

        text_score = cosine_similarity(
            resume_vector,
            job_vector
        )

        text_score_percentage = (
            text_score * 100
        )

        skill_score = calculate_skill_score(
            resume_skills,
            job["skills"]
        )


        # Combined score
        final_score = (
            text_score_percentage * 0.70
            +
            skill_score * 0.30
        )


        matched_skills = list(
            set(resume_skills) &
            set(job["skills"])
        )


        recommendations.append({

            "job": job,

            "score": final_score,

            "text_score": text_score_percentage,

            "skill_score": skill_score,

            "matched_skills": matched_skills

        })


    # -----------------------------------------------------
    # SORT RECOMMENDATIONS
    # -----------------------------------------------------

    recommendations.sort(
        key=lambda x: x["score"],
        reverse=True
    )


    # -----------------------------------------------------
    # DISPLAY RESULTS
    # -----------------------------------------------------

    st.subheader(
        "🎯 Recommended Jobs"
    )

    st.write(
        "Jobs are ranked according to how closely "
        "they match your resume."
    )


    # -----------------------------------------------------
    # TOP 5 JOBS
    # -----------------------------------------------------

    for rank, recommendation in enumerate(
        recommendations[:5],
        start=1
    ):

        job = recommendation["job"]

        score = recommendation["score"]

        matched = recommendation["matched_skills"]


        st.markdown(
            f"## {rank}. 💼 {job['title']}"
        )

        col1, col2 = st.columns(2)

        with col1:

            st.write(
                f"**🏢 Company:** {job['company']}"
            )

            st.write(
                f"**📍 Location:** {job['location']}"
            )

        with col2:

            st.write(
                f"**🎯 Match Score:** "
                f"{score:.2f}%"
            )

            st.progress(
                min(int(score), 100)
            )


        st.write(
            f"**Required Skills:** "
            f"{', '.join(job['skills']).title()}"
        )

        st.write(
            f"**Job Description:** "
            f"{job['description']}"
        )


        if matched:

            st.success(
                "Matched Skills: "
                +
                ", ".join(
                    skill.title()
                    for skill in matched
                )
            )

        else:

            st.info(
                "No direct skills matched."
            )


        st.divider()


    # -----------------------------------------------------
    # BEST RECOMMENDATION
    # -----------------------------------------------------

    best = recommendations[0]

    best_job = best["job"]


    st.success(
        f"🏆 Best Job Recommendation: "
        f"{best_job['title']} at "
        f"{best_job['company']} "
        f"— {best['score']:.2f}% Match"
    )


    # -----------------------------------------------------
    # ANALYSIS SUMMARY
    # -----------------------------------------------------

    st.subheader(
        "📊 Analysis Summary"
    )

    col1, col2, col3 = st.columns(3)

    with col1:

        st.metric(
            "Skills Detected",
            len(resume_skills)
        )

    with col2:

        st.metric(
            "Jobs Analyzed",
            len(jobs)
        )

    with col3:

        st.metric(
            "Top Match",
            f"{best['score']:.1f}%"
        )


else:

    st.info(
        "👆 Upload your PDF or DOCX resume "
        "to start the AI job analysis."
    )


# =========================================================
# FOOTER
# =========================================================

st.divider()

st.caption(
    "AI Job Recommendation System | "
    "Python + Streamlit + NLP + TF-IDF + Cosine Similarity"
)