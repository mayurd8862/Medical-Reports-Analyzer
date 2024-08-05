import streamlit as st
import google.generativeai as genai
import PIL.Image
import io

# Configure Google Generative AI with the API key
genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])

# Streamlit app title
st.title("Medical Report Analyzer")

# File uploader for medical report image
uploaded_file = st.file_uploader("Upload a medical report image:", type=["png", "jpg", "jpeg"])

if uploaded_file is not None:
    # Display the uploaded image
    img = PIL.Image.open(uploaded_file)
    st.image(img, caption="Uploaded Medical Report", use_column_width=True)
    
    if st.button("Analyze Report"):
        # Convert the uploaded image to byte array
        img_byte_arr = io.BytesIO()
        img.save(img_byte_arr, format=img.format)
        img_byte_arr = img_byte_arr.getvalue()
        
        # Generate content using Google Generative AI
        model = genai.GenerativeModel(model_name="gemini-1.5-flash")
        response = model.generate_content(["Analyse the medical report?"], img_byte_arr)
        
        # Display the response
        st.subheader("Extracted Information:")
        st.write(response.text)
else:
    st.info("Please upload a medical report image.")

