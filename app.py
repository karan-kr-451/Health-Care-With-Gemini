import google.generativeai as genai
from dotenv import load_dotenv
import os
import streamlit as st
from src.helper import *


load_dotenv()
genai.configure(api_key=os.getenv("API_KEY"))

model = genai.GenerativeModel(model_name='gemini-1.5-flash',
                              generation_config=generation_config,
                              safety_settings=safety_settings)


st.set_page_config(page_title="Health Care Assistant", page_icon="🩺", 
layout="wide")
st.title("Health Care Assistant 👨‍⚕️ 🩺 🏥")
st.subheader("An app to help with medical analysis using images")

file_uploaded = st.file_uploader('Upload the image for Analysis', 
type=['png','jpg','jpeg'])

if file_uploaded:
    st.image(file_uploaded, width=200, caption='Uploaded Image')
    
submit=st.button("Generate Analysis")

if submit:

    image_data = file_uploaded.getvalue()
    
    image_parts = [
        {
            "mime_type" : "image/jpg",
            "data" : image_data
        }
    ]
    
#     making our prompt ready
    prompt_parts = [
        image_parts[0],
        system_prompts[0],
    ]
    
#     generate response
    
    response = model.generate_content(prompt_parts)
    if response:
        st.title('Detailed analysis based on the uploaded image')
        st.write(response.text)
    