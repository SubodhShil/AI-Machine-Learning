import streamlit as st  # Correct import
import fitz  # PyMuPDF = read the contents of the pdf file
import openai
from fpdf import FPDF  # Library for generating pdf files
import os
import tempfile

# function to extract pdf file
def extract_text_from_pdf(pdf_file):
    temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".pdf")
    temp_file.write(pdf_file.read())
    temp_file.close()

    doc = fitz.open(temp_file.name)
    text = ""

    for page_num in range(len(doc)):
        page = doc.load_page(page_num)
        text += page.get_text()

    os.remove(temp_file.name)
    return text  # Ensure this function returns text

# function to ensure if it ends properly
def ensure_full_stop(text):
    text = text.strip()
    if not text.endswith(('.', '!', '?')):
        text += '.'
    return text

# function to summarize
def summarize_text(api_key, text):
    openai.api_key = api_key
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": f"Summarize the following text:\n\n{text}"}
        ],
        max_tokens=2048,
        temperature=0.5
    )

    summary = response.choices[0].message['content'].strip()
    return ensure_full_stop(summary)

# function to predict topic
def predict_topic(api_key, text):
    openai.api_key = api_key
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "system", "content": "You are a helpful assistant."},
                  {"role": "user", "content": f"What is the main topic of the following text?\n\n{text}"}],
        max_tokens=500,
        temperature=0.5
    )
    return response.choices[0].message['content'].strip()

# Function to generate a PDF
def create_pdf(summary, topic, original_file_name):
    base_name = os.path.splitext(original_file_name)[0]
    pdf_file_name = f"{base_name}_summary.pdf"

    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    pdf.cell(200, 10, txt="Summary", ln=True, align='C')
    pdf.multi_cell(0, 10, txt=summary)

    pdf.cell(200, 10, txt="Predicted Main Topic", ln=True, align='C')
    pdf.multi_cell(0, 10, txt=topic)

    pdf_file_path = f"/tmp/{pdf_file_name}"
    pdf.output(pdf_file_path)

    return pdf_file_path

# Streamlit UI
st.title("Research Paper Summary")
api_key = st.text_input("Enter your OpenAI API Key:", type="password")

uploaded_file = st.file_uploader("Upload your research paper (PDF)", type=["pdf"])

if uploaded_file is not None:
    text = extract_text_from_pdf(uploaded_file)

    if len(text) > 1000:
        summary = summarize_text(api_key, text)
        topic = predict_topic(api_key, text)

        st.subheader("Summary")
        st.write(summary)

        st.subheader("Predicted Topic")
        st.write(topic)

        if st.button("Get the Summary PDF"):
            pdf_path = create_pdf(summary, topic, uploaded_file.name)
            st.download_button(
                label="Download Summary PDF",
                data=open(pdf_path, "rb").read(),
                file_name=os.path.basename(pdf_path),
                mime="application/pdf"
            )
    else:
        st.warning("The document is too short for meaningful analysis.")
else:
    st.info("Please upload a valid PDF file to proceed.")