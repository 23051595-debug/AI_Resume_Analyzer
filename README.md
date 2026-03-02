 # AI Resume Analyzer & Job Matcher
An intelligent web application built using **Streamlit, NLP, and Machine Learning** that analyzes resumes against job descriptions, calculates matching scores, extracts skills, identifies missing skills, and provides actionable feedback along with resume bullet rewriting suggestions.
# Features

-  Upload resume in **PDF format**
-  AI-powered **semantic similarity matching**
-  Resume-to-job **matching score calculation**
-  **Skill extraction** from resume and job description
-  Identification of **missing skills**
-  AI-powered **resume bullet point rewriting**
-  Personalized **resume improvement suggestions**
# Tech Stack
- Python
- Streamlit – Frontend UI
- NLTK – Text preprocessing
- Sentence Transformers – Semantic similarity
- Scikit-learn – Cosine similarity
- PDFPlumber – PDF text extraction
# Installation & Setup

# 1.Clone the Repository

bash-
git clone https://github.com/your-username/ai-resume-analyzer.git
cd ai-resume-analyzer

# 2.Create Virtual Environment (Optional but Recommended)

bash-
python -m venv venv
Activate:

Windows:
bash-
venv\Scripts\activate



# 3.Install Dependencies

bash
pip install -r requirements.txt
# 4.Run the Application

bash
streamlit run app.py
Open browser → `http://localhost:8501`
# How It Works
1. Extracts resume text from PDF
2. Cleans and preprocesses text using NLP
3. Computes semantic similarity score
4. Extracts technical skills
5. Detects missing skills
6. Generates improvement feedback
7. Rewrites resume bullet points using AI logic
# Project Structure
ai-resume-analyzer/
│
├── app.py
├── requirements.txt
├── README.md
└── sample_resume.pdf (optional)
# Use Cases
- Students preparing for placements
- Job seekers improving resumes
- Resume-job matching analysis
- Career guidance & upskilling suggestions
# Screenshots

<img width="1850" height="820" alt="Screenshot 2026-03-02 230150" src="https://github.com/user-attachments/assets/0ecdf4ee-53e2-45f9-9d1f-01bab23c366f" />
<img width="1822" height="787" alt="Screenshot 2026-03-02 230135" src="https://github.com/user-attachments/assets/0851212c-6f8c-45d4-b87c-f7af2823813b" />
<img width="1844" height="752" alt="Screenshot 2026-03-02 230128" src="https://github.com/user-attachments/assets/ea2347ef-78cb-45dd-90b2-4a2065008ee4" />
<img width="1837" height="869" alt="Screenshot 2026-03-02 230102" src="https://github.com/user-attachments/assets/0cd98f9b-fef9-4071-806d-cdcb29d550b3" />


---

# Future Improvements
- GPT-powered resume rewriting
- ATS score optimization
- Resume ranking system
- JD-based resume customization
- Skill gap learning roadmap
# Contribution

Contributions are welcome!  
Fork the repo → Improve → Submit PR
# License

This project is licensed under the MIT License.
# Developed By

Kajal Yadav  
 B.Tech CSE Student | KIIT University  
 AI | ML | Data Science | Full Stack  

If You Like This Project

Give it a star on GitHub — it motivates a lot!
