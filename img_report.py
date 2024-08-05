
import streamlit as st

import google.generativeai as genai
import PIL.Image

# genai.configure(api_key=os.environ["GOOGLE_API_KEY"])
genai.configure(api_key=st.secrets.GOOGLE_API_KEY)
img = PIL.Image.open('image.png')

model = genai.GenerativeModel(model_name="gemini-1.5-flash")
response = model.generate_content(["Analyse the medical report?", img])
print(response.text)
