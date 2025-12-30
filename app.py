import streamlit as st
from dotenv import load_dotenv

from chains.question_chain import get_question_chain
from utils.text_cleaner import clean_text

load_dotenv()

def add_bg_image():
    st.markdown(
        """
        <style>
        .stApp {
            background-image: url("https://images.unsplash.com/photo-1557683316-973673baf926");
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
        }
        .block-container {
            background-color: rgba(255, 255, 255, 0.88);
            padding: 2rem;
            border-radius: 15px;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

add_bg_image()

st.markdown(
    "<h1 style='text-align: center;'>🤖 AI Interview Question Generator</h1>",
    unsafe_allow_html=True
)

st.markdown(
    "<p style='text-align: center;'>Generate role-specific interview questions using AI</p>",
    unsafe_allow_html=True
)

st.markdown("## 🎯 Enter Your Details")

col1, col2 = st.columns(2)

with col1:
    role = st.text_input("💼 Job Role", placeholder="Data Science Intern")

with col2:
    skills = st.text_input("🛠️ Skills", placeholder="Python, SQL, Machine Learning")

st.markdown("")

if st.button("✨ Generate Interview Questions"):
    if role and skills:
        role = clean_text(role)
        skills = clean_text(skills)

        with st.spinner("Generating questions... ⏳"):
            chain = get_question_chain()
            response = chain.invoke({
                "role": role,
                "skills": skills
            })

        st.success("Questions generated successfully 🎉")
        st.markdown("### 📋 Interview Questions")
        st.write(response.content)

    else:
        st.error("Please fill in both Job Role and Skills ⚠️")
