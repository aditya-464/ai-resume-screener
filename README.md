# 📝 AI Resume Screener

A **Generative AI-powered Resume Screening tool** that automatically ranks resumes based on semantic similarity to a job description using **NLP embeddings**.  


---

## 🚀 Features
- Upload multiple resumes in **PDF, DOCX, or TXT** formats  
- Automatically rank resumes based on **job description relevance**  
- Uses **sentence-transformers** for semantic similarity  
- Simple **React + Vite** frontend for uploading files and viewing results  
- Minimalistic, **no CSS/UI frameworks**  

---

## 🌐 Areas of Application
The AI Resume Screener can be applied in **recruitment**, **HR automation**, and **talent management**. It helps in **automatically screening candidates**, saving time for HR teams. It can also be extended to **job portals**, **freelance platforms**, or **internal hiring tools** to rank applicants efficiently.

---

## 🧩 Tech Stack
- **Backend:** Python, Flask, `sentence-transformers`, `scikit-learn`, `pypdf`, `python-docx`  
- **Frontend:** React + Vite  
- **Language:** Python, JavaScript  

---


## 💻 Setup Instructions


### 1️⃣ Clone the Repository
```bash
# Clone the repository
git clone https://github.com/aditya-464/ai-resume-screener.git

# Go into the project directory
cd ai-resume-screener
```

### 2️⃣ Backend Setup

```bash
cd backend
python -m venv venv

# Activate virtual environment
# Linux / Mac:
source venv/bin/activate
# Windows:
venv\Scripts\activate

pip install -r requirements.txt
python app.py
```

### 3️⃣ Frontend Setup
```bash
cd frontend
npm install
npm run dev
```

---

## ⚡ How to Use

- Enter the job description in the textarea.
- Upload one or multiple resumes (PDF/DOCX/TXT).
- Click Analyze Resumes.
- View ranked resumes with similarity scores.

