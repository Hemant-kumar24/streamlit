import streamlit as st
import google.generativeai as genai

def solver(question):
    genai.configure(api_key="AIzaSyC5bXWjvFHzsy0xVsD_RTVPm_hl9wNTeRY")
    model=genai.GenerativeModel("gemini-1.5-flash")
    response=model.generate_content(question)
    return response.text
st.balloons()
st.snow()
st.header("SIMPLE  CHATGPT ⭕💕")
st.header("Feel Free To Ask Anything 😊")
question=st.text_input("Ask Anything ❓","hello")
ans=solver(question)
st.text_area("Your Answer is Here 👇",ans,height=500)



