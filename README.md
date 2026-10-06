# AI Job Recommendation System

## 📌 Project Overview

The AI Job Recommendation System is a Python-based web application that analyzes a user's resume and recommends suitable job roles based on their skills, experience, and resume content.

The system uses Natural Language Processing (NLP) concepts such as TF-IDF and Cosine Similarity to compare the uploaded resume with predefined job descriptions and generate personalized job recommendations.

---

## 🎯 Objectives

- Analyze uploaded resumes automatically.
- Extract relevant technical skills from resumes.
- Compare resume content with different job descriptions.
- Calculate job-resume matching scores.
- Recommend the most suitable job roles.
- Identify skills that match the selected job.
- Provide a simple and user-friendly interface.

---

## ✨ Features

- 📄 Upload Resume
- Supports PDF and DOCX resumes
- 🔍 Resume Text Extraction
- 🧠 Skill Detection
- 🎯 Job Recommendation
- 📊 Job Matching Score
- 🏆 Top 5 Recommended Jobs
- 💡 Matched Skills Display
- 📈 Resume Analysis
- 🖥️ Interactive Streamlit Interface

---

## 🛠️ Technologies Used

### Programming Language
- Python

### Frontend / Web Framework
- Streamlit

### NLP / Machine Learning Concepts
- Natural Language Processing
- TF-IDF
- Cosine Similarity
- Text Matching
- Skill Extraction

### Python Libraries
- Streamlit
- Pandas
- NumPy
- PyPDF
- python-docx
- Collections
- Math

---

## 📂 Project Structure

```text
AI_Job_Recommendation_System/
│
├── app.py
├── README.md
├── requirements.txt
│
├── venv/
│
└── resumes/
```

> Note: The exact files and folders may differ depending on your project version.

---

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/AI_Job_Recommendation_System.git
```

### 2. Open the Project Folder

```bash
cd AI_Job_Recommendation_System
```

### 3. Create a Virtual Environment

```bash
python -m venv venv
```

### 4. Activate the Virtual Environment

For Windows:

```powershell
venv\Scripts\activate
```

### 5. Install Required Libraries

```bash
python -m pip install -r requirements.txt
```

---

## ▶️ How to Run

Activate the virtual environment:

```powershell
venv\Scripts\activate
```

Run the Streamlit application:

```powershell
python -m streamlit run app.py
```

The application will open in the browser at:

```text
http://localhost:8501
```

---

## 🔄 How the System Works

```text
User Uploads Resume
        ↓
Resume Text Extraction
        ↓
Skill Detection
        ↓
Text Preprocessing
        ↓
TF-IDF Calculation
        ↓
Cosine Similarity
        ↓
Job Matching
        ↓
Calculate Match Score
        ↓
Rank Job Roles
        ↓
Display Top Job Recommendations
```

---

## 🧠 Matching Method

The system compares the resume with predefined job descriptions.

### TF-IDF

TF-IDF stands for:

**Term Frequency – Inverse Document Frequency**

It determines the importance of words in a document.

### Cosine Similarity

Cosine Similarity measures how similar the resume is to a particular job description.

The similarity score is combined with the skill matching score to generate the final recommendation score.

```text
Final Score =
(Text Similarity × 70%) +
(Skill Match × 30%)
```

---

## 💼 Example Job Roles

The system can recommend roles such as:

- Python Developer
- Web Developer
- Data Analyst
- Machine Learning Engineer
- Software Developer
- Frontend Developer
- Backend Developer
- Data Scientist
- Java Developer
- AI Engineer

---

## 📊 Example Output

```text
Top Recommended Jobs

1. Python Developer       87%
2. Software Developer     82%
3. Web Developer           78%
4. Data Analyst            71%
5. AI Engineer             65%
```

The system also displays the skills detected from the uploaded resume and the skills matching each job role.

---

## 🔮 Future Enhancements

The project can be extended with:

- Resume Score
- Skill Gap Analysis
- Job Category Filtering
- Resume Improvement Suggestions
- Learning Recommendations
- Interactive Charts
- PDF Recommendation Report
- Real-time Job API Integration
- AI-powered Resume Analysis
- Personalized Career Suggestions

---

## 🎓 Project Purpose

This project was developed as an academic and placement-oriented project to demonstrate practical knowledge of:

- Python Programming
- Web Application Development
- Natural Language Processing
- Machine Learning Concepts
- Data Processing
- Resume Analysis
- Problem Solving

---

## 👩‍💻 Author

**Asa Sneha**

B.Tech – Computer Science Engineering

---

## 📜 License

This project is created for educational and academic purposes.