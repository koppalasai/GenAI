import os
import google.generativeai as genai
import streamlit as st
from PIL import Image 
os.environ["GOOGLE_API_KEY"]="AIzaSyCECtnn08CfZmGASBs3tREmpjXo-ol8N0M"
genai.configure(api_key=os.environ["GOOGLE_API_KEY"])
model=genai.GenerativeModel("gemini-1.5-pro")
def generate(image,prompt):
    response=model.generate_content([image,prompt])
    return response.text
st.title("Lens")
image=st.file_uploader("upload the image",type=["jpeg","png"])
input_text=st.text_input("enter prompt")
button=st.button("click")
if image and input_text and button:
    im=Image.open(image)
    st.image(im)
    st.write(generate(im,input_text))


