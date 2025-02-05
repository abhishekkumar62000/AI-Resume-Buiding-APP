import streamlit as st # type: ignore
import os
from openai import OpenAI # type: ignore
import pdfkit # type: ignore
from io import BytesIO

# OpenAI API Key Setup
os.environ["OPENAI_API_KEY"] = "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"
client = OpenAI()

def generate_resume(name, skills, experience, job_role):
    prompt = f"""
    Create a professional resume for {name} applying for {job_role}. 
    Skills: {skills}. Experience: {experience}.
    Format it properly.
    """
    
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "system", "content": "You are a resume expert."},
                  {"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content

# Streamlit UI
st.title("AI-Powered Resume Generator")

name = st.text_input("Your Name")
skills = st.text_area("Your Skills (comma-separated)")
experience = st.text_area("Your Experience")
job_role = st.text_input("Job Role")

if st.button("Generate Resume"):
    if name and skills and experience and job_role:
        resume_text = generate_resume(name, skills, experience, job_role)
        st.subheader("Generated Resume")
        st.text_area("", resume_text, height=300)
        
        # Convert to PDF
        pdf = BytesIO()
        pdf.write(resume_text.encode("utf-8"))
        st.download_button("Download Resume as PDF", pdf, f"{name}_resume.pdf", "application/pdf")
    else:
        st.error("Please fill all fields!")

st.sidebar.write("Developer: Abhishek Kumar")
