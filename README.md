# 🧠 AI-Powered Resume Optimizer

![Python](https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge&logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![Groq](https://img.shields.io/badge/Groq-LLaMA_3.3_70B-orange?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

A Streamlit web application that analyzes your resume against a job description using LLaMA 3.3 70B via Groq API. Get an instant score, missing keywords, actionable suggestions, and an AI-generated summary — all in a sleek dark UI.

---

## 📸 Screenshots

<img width="1356" height="732" alt="image" src="https://github.com/user-attachments/assets/e4443702-cc60-4af6-96f7-d6022bfe6787" />


| Upload & Analyze | Results Dashboard |
|------------------|-------------------|
| ![upload](<img width="1201" height="802" alt="Screenshot 2026-04-21 131033" src="https://github.com/user-attachments/assets/9cdbe78a-e907-4578-852c-506ecce931e5" />
) | 
![results](<img width="1118" height="816" alt="image" src="https://github.com/user-attachments/assets/6360f5ab-cc9e-4535-9c33-35a8f6464360" />
) |

---

## ✨ Features

- 📄 **PDF Resume Parsing** — Extracts and processes resume content from uploaded PDFs
- 🎯 **Keyword Gap Analysis** — Identifies missing keywords compared to the job description
- 📊 **Resume Score** — Rates your resume from 1 to 10 with a visual indicator
- 💡 **Actionable Suggestions** — Point-by-point improvement recommendations
- 🧠 **AI Summary** — A natural language vibe-check of your resume fit
- ⚡ **Fast Inference** — Powered by Groq's ultra-fast LLaMA 3.3 70B model
- 🔒 **Temporary File Handling** — Uploaded PDFs are never stored permanently

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|------------|
| Frontend | Streamlit |
| PDF Parsing | pymupdf4llm |
| LLM | LLaMA 3.3 70B via Groq API |
| Language | Python 3.10+ |
| Hosting | Streamlit Cloud |

---

## 🚀 Getting Started

### Prerequisites

- Python 3.10+
- A free [Groq API Key](https://console.groq.com)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/Sahib-Chhabra1908/ai-resume-optimizer.git
   cd ai-resume-optimizer
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up your API key**

   Create a `.env` file in the project root:
   ```
   GROQ_API_KEY=gsk_your-key-here
   ```

4. **Run the app**
   ```bash
   streamlit run app.py
   ```

---

## 📦 Requirements

```
streamlit
pymupdf4llm
requests
python-dotenv
```

---

## 🔐 Environment Variables

| Variable | Description |
|----------|-------------|
| `GROQ_API_KEY` | Your Groq API key from [console.groq.com](https://console.groq.com) |

For Streamlit Cloud deployment, add this under **Settings → Secrets**:
```toml
GROQ_API_KEY = "gsk_your-key-here"
```

---

## 📁 Project Structure

```
ai-resume-optimizer/
├── app.py               # Main Streamlit application
├── requirements.txt     # Python dependencies
├── .env                 # Local environment variables (not committed)
├── .gitignore           # Git ignore rules
└── README.md            # Project documentation
```

---

## 🤝 Contributing

Contributions are welcome! Here's how to get started:

1. Fork the repository
2. Create a new branch: `git checkout -b feature/your-feature-name`
3. Make your changes and commit: `git commit -m "Add your feature"`
4. Push to your branch: `git push origin feature/your-feature-name`
5. Open a Pull Request

Please make sure your code is clean and tested before submitting.

---

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## 👤 Author

**Sahib Chhabra**  
GitHub: [@Sahib-Chhabra1908](https://github.com/Sahib-Chhabra1908)
