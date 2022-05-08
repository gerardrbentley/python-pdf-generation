from datetime import date
import json
import streamlit as st
import urllib3

http = urllib3.PoolManager()

st.set_page_config(layout="centered", page_icon="🎓", page_title="Diploma Generator")
st.title("🎓 Diploma PDF Generator")

st.write(
    "This app shows you how you can use Streamlit to make a PDF generator app in just a few lines of code!"
)

left, right = st.columns(2)

right.write("Here's the template we'll be using:")

right.image("template.png", width=300)

left.write("Fill in the data:")
form = left.form("template_form")
student = form.text_input("Student name")
course = form.selectbox(
    "Choose course",
    ["Report Generation in Streamlit", "Advanced Cryptography"],
    index=0,
)
grade = form.slider("Grade", 1, 100, 60)
submit = form.form_submit_button("Generate PDF")

if submit:
    payload = {
        "student": student,
        "course": course,
        "grade": grade,
        "completed_date": date.today().isoformat(),
    }
    response = http.request(
        "POST",
        "http://pdf-backend:8000/diploma",
        body=json.dumps(payload),
        headers={"Content-Type": "application/json"},
    )
    pdf = response.data
    st.balloons()
    st.write(pdf)

    right.success("🎉 Your diploma was generated!")

    right.download_button(
        "⬇️ Download PDF",
        data=pdf,
        file_name="diploma.pdf",
        mime="application/octet-stream",
    )
