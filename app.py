import streamlit as st
import google.generativeai as genai
import PIL.Image


st.title("🩺 Medical Reports Analyzer")

# genai.configure(api_key=os.environ["GOOGLE_API_KEY"])
genai.configure(api_key=st.secrets.GOOGLE_API_KEY)

# File uploader for medical report images (multiple)
uploaded_file = st.file_uploader("Upload medical report images:", type=["png", "jpg", "jpeg"], )

    
prompt = f"""
You are an AI model that analyzes medical reports. Analyze the following report given by image to extract relevant information in a structured way, ensuring no personally identifiable information is included. Ensure the extracted data is accurate and appropriate for validation by health professionals.
Provide a professional and concise conclusion at the end, summarizing the overall health status of the patient and any critical issues that need attention.
"""

if uploaded_file is not None:
    # Display the uploaded image
    img = PIL.Image.open(uploaded_file)
    st.image(img, caption="Uploaded Medical Report", use_column_width=True)
    
    model = genai.GenerativeModel(model_name="gemini-1.5-flash")
    response = model.generate_content([prompt, img])
    st.write(response.text)

