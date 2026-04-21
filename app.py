import streamlit as st
import pymupdf4llm as text_e
import os
import json
import tempfile
import requests

def analyze_resume(resume_text, job_description):
    prompt = f"""
    Analyze this Resume against the Job Description. 
    Return a JSON dictionary with these keys:
    - 'score': (int 1-10)
    - 'missing_keywords': (list of strings,in form of strings like "Creative,Handsome,etc...")
    - 'suggestions': (a string in points)
    - 'vibe': (string summary)

    Return ONLY raw JSON, no markdown, no backticks.

    Resume: {resume_text}
    JD: {job_description}
    """
    
    response = requests.post(
        url="https://api.groq.com/openai/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {st.secrets["GROQ_API_KEY"]}",
            "Content-Type": "application/json"
        },
        json={
            "model": "llama-3.3-70b-versatile",
            "messages": [{"role": "user", "content": prompt}]
        }
    )
    
    text = response.json()["choices"][0]["message"]["content"]
    text = text.strip().removeprefix("```json").removesuffix("```").strip()
    return json.loads(text)

st.markdown("""
    <style>
    .stApp {
        background-color: #0d1117;
        color: #c9d1d9;
    }
    .stHeading h1 {
        color: #58a6ff !important;
        text-align: center;
        font-family: monospace;
        letter-spacing: 2px;
        margin-bottom: 30px;
    }
    .hud-card {
        background-color: #161b22;
        border: 1px solid #30363d;
        border-radius: 12px;
        padding: 25px;
        margin-bottom: 20px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.2);
    }
    .score-container {
        text-align: center;
        background: linear-gradient(145deg, #1f242c, #161b22);
        border: 1px solid #30363d;
        border-radius: 12px;
        padding: 30px;
        height: 100%;
    }
    .keyword-pill {
        display: inline-block;
        background-color: rgba(88, 166, 255, 0.1);
        color: #58a6ff;
        border: 1px solid #58a6ff;
        padding: 6px 16px;
        border-radius: 20px;
        margin: 5px;
        font-size: 15px;
        font-weight: 600;
    }
    div.stButton > button {
        width: 100%;
        border-radius: 8px;
        font-weight: bold;
        border: 1px solid #388bfd;
        color: #58a6ff;
        background: transparent;
        transition: 0.3s;
    }
    div.stButton > button:hover {
        background: #388bfd;
        color: white;
    }
    </style>
""", unsafe_allow_html=True)

st.title("AI-POWERED RESUME OPTIMIZER")

file = st.file_uploader("Upload a file", type="pdf")
job = st.text_area("Enter the Job description: ", height=150)

if st.button("Optimize Resume"):
    if bool(file) == True and bool(job) == True:
        progress_bar = st.progress(0, text="System Booting...")

        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
            tmp.write(file.getbuffer())
            tmp_path = tmp.name

        st.markdown("#### 🔍 Scanning PDF structure...")
        progress_bar.progress(25, text="Extracting Markdown...")
        text = text_e.to_markdown(tmp_path)
        os.remove(tmp_path)

        st.markdown("#### 📈 Generating Dashboard...")
        progress_bar.progress(90, text="Finalizing report...")
        al = analyze_resume(text, job)

        progress_bar.empty()
        st.toast("The task is done", icon="🎉")

        st.markdown("---")
        st.header("📊 #AI Analyzes:")

        col1, col2 = st.columns([1, 2])

        with col1:
            if al['score'] >= 8:
                color = "#3fb950"
                status = "Top-Notch 😍"
                gif_url = "https://media.giphy.com/media/3o7TKqFZJpwL8Giz2E/giphy.gif"
            elif al['score'] >= 5:
                color = "#d29922"
                status = "Maza Nhi Aaya 😑"
                gif_url = "https://media.giphy.com/media/l0HlvtIPzPdt2usKs/giphy.gif"
            else:
                color = "#f85149"
                status = "Ye toh Tatti hai 💩"
                gif_url = "https://media.giphy.com/media/xT5LMzIK1AdZJ4cYW4/giphy.gif"

            st.markdown(f"""
            <div class="score-container">
                <h1 style='color:{color}; font-size:65px; margin:0;'>{al['score']}</h1>
                <h3 style='color:#c9d1d9; margin-top: 10px; margin-bottom: 20px;'>Status: {status}</h3>
                <img src="{gif_url}" style="width: 100%; max-height: 180px; object-fit: cover; border-radius: 8px; border: 1px solid #30363d; box-shadow: 0 4px 10px rgba(0,0,0,0.3);">
            </div>
            """, unsafe_allow_html=True)

        with col2:
            pills_html = "".join([f'<span class="keyword-pill">{kw}</span>' for kw in al['missing_keywords']])
            st.markdown(f"""
            <div class="hud-card" style="height: 100%;">
                <h3 style="color: #58a6ff; margin-top: 0;">🎯 Missing Keywords</h3>
                <div style="margin-top: 15px;">{pills_html}</div>
            </div>
            """, unsafe_allow_html=True)

        st.markdown(f"""
        <div class="hud-card">
            <h3 style="color: #58a6ff; margin-top: 0;">💡 Suggestions:</h3>
            <div style="font-size: 16px; line-height: 1.6; white-space: pre-wrap; margin-top: 15px;">{al['suggestions']}</div>
        </div>
        """, unsafe_allow_html=True)

        st.markdown(f"""
        <div class="hud-card" style="border-left: 4px solid #58a6ff;">
            <h3 style="color: #58a6ff; margin-top: 0;">🧠 AI-Summary:</h3>
            <div style="font-size: 16px; line-height: 1.6; white-space: pre-wrap; margin-top: 15px;">{al['vibe']}</div>
        </div>
        """, unsafe_allow_html=True)

        if st.button("Reload Page"):
            st.rerun()

    else:
        st.warning("PLEASE UPLOAD A FILE/ENTER JOB DESCRIPTION TO CONTINUE!!!")