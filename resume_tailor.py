from dotenv import load_dotenv
load_dotenv()
import streamlit as st
from mardown_2_pdf.markdown2pdf import markdown2pdf
from crew.main import extractor_crew
from pdfminer.high_level import extract_text
import base64

# Set the title of the app
st.title('Resume and Job Description Input')

# Add a header
st.header('Upload your resume and provide the job description URL')

# File uploader for PDF (resume)
uploaded_file = st.file_uploader("Upload your resume (PDF)", type="pdf")

# Text input for job description URL
job_description_url = st.text_input("Enter the job description URL")

# Store the inputs and process them
if uploaded_file and job_description_url:
    # Store the uploaded file and URL
    st.session_state['resume'] = uploaded_file
    st.session_state['job_description_url'] = job_description_url
    st.success("Inputs have been stored successfully!")

    # Save the uploaded file to a temporary location
    with open("temp_resume.pdf", "wb") as f:
        f.write(uploaded_file.getbuffer())

    resume_content = extract_text("temp_resume.pdf")

    # Prepare inputs for the extractor_crew
    inputs = {
        'job_posting_url': job_description_url,
        'resume_content': resume_content,
    }

    # Call the extractor_crew.kickoff function
    result = extractor_crew.kickoff(inputs=inputs)

    if markdown2pdf():
        st.success("Your PDF has been created successfully!")
        pdf_path = 'your_resume.pdf'
        
        # Display the PDF to the user
        with open(pdf_path, "rb") as pdf_file:
            base64_pdf = base64.b64encode(pdf_file.read()).decode('utf-8')
            pdf_display = f'<embed src="data:application/pdf;base64,{base64_pdf}" width="700" height="1000" type="application/pdf">'
            st.markdown(pdf_display, unsafe_allow_html=True)
        
        # Provide a download button for the PDF
        with open(pdf_path, "rb") as pdf_file:
            PDFbyte = pdf_file.read()
            st.download_button(label="Download Modified Resume",
                               data=PDFbyte,
                               file_name="modified_resume.pdf",
                               mime='application/octet-stream')
    else:
        st.error("Something went wrong, please try again!")
        


# Display stored inputs if available
if 'resume' in st.session_state and 'job_description_url' in st.session_state:
    st.subheader("Stored Inputs")
    st.write("Resume PDF:", st.session_state['resume'].name)
    st.write("Job Description URL:", st.session_state['job_description_url'])
