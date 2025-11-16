# 🤖 Agentic AI Research Assistant

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Flask](https://img.shields.io/badge/Flask-3.0+-green.svg)
![Gemini](https://img.shields.io/badge/Gemini-2.0%20Flash-orange.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

An **AI-powered research assistant** built using **Flask** and **Gemini API**, designed to automatically generate a structured **Research Plan**, conduct in-depth **Research**, and produce a concise **Summary** — all within a clean, minimal web interface.

---

## 🌟 Features

✅ **Natural Language Research**  
Type any topic or question — the app automatically researches it using Gemini.

✅ **Structured Output**  
Responses are split into:
- **Research Plan** (AI's reasoning steps)
- **Research Results** (organized under key sections)
- **Summary** (concise overview)

✅ **Modern UI**  
Simple and responsive design using HTML/CSS — includes fade-in animations, styled cards, and keyboard shortcuts.

✅ **Agentic Workflow Ready**  
Built modularly — can be extended with multiple specialized AI agents (Planner, Researcher, Summarizer).

---

## 🧩 Project Structure

```
Research Agent 3/
│
├── app/
│   ├── __init__.py              # Flask app factory
│   ├── main.py                  # Main blueprint + routes
│   └── researcher_agent.py      # Handles Gemini AI calls
│
├── static/
│   └── css/
│       └── style.css            # App styling
│
├── templates/
│   └── index.html               # Main front-end template
│
├── .env                         # API keys and secrets
├── app.py                       # Flask app entry point
├── requirements.txt             # Python dependencies
└── README.md                    # Documentation
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/Saikiranabhi/Ai_Research_Assistant.git
cd Ai_Research_Assistant
```

### 2️⃣ Create and Activate a Virtual Environment

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

**Required packages (requirements.txt):**
```
Flask==3.0.0
python-dotenv==1.0.0
google-generativeai==0.3.0
```

### 4️⃣ Configure Environment Variables

Create a `.env` file in the project root:

```env
GEMINI_API_KEY=your_actual_gemini_api_key
SECRET_KEY=your_flask_secret_key
```

**To get your Gemini API key:**
1. Visit [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Sign in with your Google account
3. Create a new API key
4. Copy and paste it into your `.env` file

---

## 🚀 Running the App

### Start the Flask Server

```bash
python app.py
```

The application will start on:
👉 **http://127.0.0.1:5000/**

Open this URL in your browser to access the research assistant.

---

## 🧠 How It Works

### 🧩 1. Input
You enter a research query, such as:
> "How is AI being used in healthcare today?"

### 🧩 2. Research Pipeline
- The app calls the **Gemini 2.0 Flash** model via `google.generativeai`
- The `run_research()` function prompts Gemini to:
  - Explain key concepts
  - List recent developments, papers, and resources
  - Summarize future directions

### 🧩 3. Display
- **Research Plan** is extracted and displayed as an ordered list
- **Research Results** section is formatted with bullet points and line breaks
- **Summary** provides a compact view of the overall findings

---

## 🧱 Example Output

### Input:
```
How is AI being used in recent days?
```

### Output:

#### **Research Plan**
1. Identify core AI application domains
2. Gather recent papers, open-source tools, and industry trends
3. Summarize ongoing challenges and future research paths

#### **Research Results**

**1️⃣ Key Concepts**
- Machine Learning enables systems to learn patterns from data
- Deep Learning uses neural networks for complex pattern recognition
- NLP and Computer Vision power conversational and visual AI

**2️⃣ Recent Developments**
- Multimodal AI (e.g., GPT-4, Gemini, LLaMA 3)
- Agentic AI frameworks (LangChain, CrewAI, AutoGen)
- Open-source LLMs improving accessibility

**3️⃣ Future Directions**
- Explainability, Energy efficiency, and AI safety
- Continued evolution of multi-agent reasoning

#### **Summary**
AI is rapidly advancing across healthcare, finance, and creative industries. Recent developments focus on multimodal capabilities and agentic workflows, with ongoing emphasis on safety and interpretability.

---

## 🧰 Tech Stack

| Component | Description |
|-----------|-------------|
| **Backend** | Flask (Python) |
| **AI Engine** | Gemini 2.0 Flash |
| **Frontend** | HTML5, CSS3 |
| **Environment** | `.env` for secrets |
| **Libraries** | `google-generativeai`, `python-dotenv`, `Flask` |

---

## 🧑‍💻 Extending the Project

You can easily expand this project by adding:

- **planner_agent.py** – Generates structured research steps before execution
- **summarizer_agent.py** – Condenses multi-agent results into key insights
- **database.py** – Logs queries and results to MongoDB or SQLite for history
- **Front-end Enhancements** – Add animations, export results (PDF/Markdown), or dark/light theme toggle
- **Multi-Agent System** – Implement CrewAI or LangGraph for advanced workflows

---

## ⚠️ Common Issues

| Problem | Cause | Fix |
|---------|-------|-----|
| `NameError: run_research not defined` | Function not imported | Ensure `from app.researcher_agent import run_research` is in `main.py` |
| HTML showing `<br>` instead of line breaks | Using `<pre>` tag | Replace `<pre>` with `<div>` and use proper CSS |
| `ImportError: cannot import main_bp` | Blueprint missing | Define `main_bp = Blueprint('main', __name__)` in `main.py` |
| Gemini errors / API failure | Missing/invalid API key | Check `.env` file and verify API key validity |
| Port already in use | Another app using port 5000 | Change port in `app.py`: `app.run(port=5001)` |

---

## 📝 API Usage

The application uses the Gemini API with the following configuration:

```python
import google.generativeai as genai

genai.configure(api_key=os.getenv('GEMINI_API_KEY'))
model = genai.GenerativeModel('gemini-2.0-flash-exp')
```

**Rate Limits:** Free tier includes 15 requests per minute. For production use, consider upgrading to a paid plan.

---

## 🔒 Security Notes

- **Never commit `.env` files** to version control
- Add `.env` to your `.gitignore` file
- Rotate API keys regularly
- Use environment variables for all sensitive data
- Consider implementing rate limiting for production deployments

---

## 📄 License

This project is released under the **MIT License**.

```
MIT License

Copyright (c) 2025 Kiran

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

---

## 💡 Author

**Kiran**  
🎓 Student & AI Developer  
Building smart agentic tools with LLMs, Flask, and modern AI frameworks.

---

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📧 Support

If you encounter any issues or have questions:
- Open an issue on GitHub
- Contact: [your-email@example.com]

---

## 🙏 Acknowledgments

- **Google Gemini** for providing the powerful AI API
- **Flask** community for the excellent web framework
- All contributors and users of this project

---

**⭐ If you find this project helpful, please consider giving it a star!**
