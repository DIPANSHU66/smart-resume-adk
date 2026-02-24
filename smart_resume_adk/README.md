# Smart Resume Analyzer (Multi-Agent System using Google ADK)

## 📌 Problem
This system analyzes a resume against a job description and suggests keyword improvements to improve ATS compatibility.

## 🧠 Architecture
The system follows a multi-agent orchestration pattern:

- Root Agent (resume_orchestrator)
- Resume Parsing Agent
- Job Description Analysis Agent
- Keyword Optimization Agent

Pattern Used:
Sequential Orchestration (Parse → Analyze → Optimize)

## 🛠 Tools Used
- Built-in google_search tool (ADK)
- extract_resume_text()
- keyword_match_score()
- generate_markdown_report()

## 🚀 Setup Instructions

```bash
git clone <repo-url>
cd smart_resume_adk
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt