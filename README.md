# 🚀 AI Interview Copilot

An AI-powered interview preparation platform that helps job seekers analyze their resumes, compare them with job descriptions, generate interview questions, evaluate answers, and download detailed interview reports.

Built using **Python**, **Streamlit**, **Groq LLM (Llama 3.3)**, **SQLite**, **ReportLab**, and **Docker**.

---

## ✨ Features

- 📄 Resume PDF Parsing
- 🤖 AI-Powered Resume Analysis
- 🎯 Job Description Matching
- 💬 AI Interview Question Generation
- 📝 Answer Evaluation and Feedback
- 📑 PDF Report Generation
- 🗄️ SQLite Database Storage
- 🐳 Dockerized Deployment
- ☁️ Deployed on Render

---

## 🛠️ Tech Stack

- Python
- Streamlit
- Groq API (Llama 3.3)
- SQLite
- ReportLab
- Docker
- Git & GitHub
- Render

---

## 📂 Project Structure

```
AI-Interview-Copilot/
│
├── app.py
├── requirements.txt
├── Dockerfile
├── README.md
├── database.db
│
├── modules/
│   ├── resume_parser.py
│   ├── resume_analyzer.py
│   ├── interview_generator.py
│   ├── answer_evaluator.py
│   ├── pdf_report.py
│   └── database.py
│
├── uploads/
├── reports/
└── assets/
```

---

## 🚀 Run Locally

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/AI-Interview-Copilot.git
cd AI-Interview-Copilot
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure Environment Variables

Create a `.env` file and add your Groq API key.

```env
GROQ_API_KEY=your_api_key_here
```

### 4. Start the Application

```bash
streamlit run app.py
```

---

## 🐳 Run with Docker

### Build the Docker Image

```bash
docker build -t ai-interview-copilot .
```

### Run the Container

```bash
docker run -p 8501:8501 ai-interview-copilot
```

Open your browser:

```
http://localhost:8501
```

---

## ☁️ Live Demo

The application is deployed on **Render**.

**Live URL:**

```
https://your-render-url.onrender.com
```

---

## 📋 How It Works

1. Upload your resume in PDF format.
2. Enter the target job description.
3. AI analyzes your resume and compares it with the job description.
4. Generates personalized interview questions.
5. Evaluate your answers with AI-powered feedback.
6. Download a detailed PDF interview report.

---

## 📈 Future Improvements

- Voice-based mock interviews
- ATS Resume Score
- Multiple resume support
- HR behavioral interview mode
- Performance analytics dashboard
- Authentication and user accounts

---

## 👨‍💻 Author

**Shailesh Bahirat**

GitHub: https://github.com/your-username
