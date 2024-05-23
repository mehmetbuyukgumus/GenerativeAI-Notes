from openai import OpenAI
import os
from dotenv import load_dotenv
import streamlit as st

load_dotenv()

my_keys = os.getenv("openai_api_key")

client = OpenAI(api_key=my_keys)

if "messages" not in st.session_state:
    st.session_state.messages = []
    st.session_state.messages.append({"role": "system","content": "Senin adın Mehmet Büyükgümüş ve sen beni taklit eden bir insan kaynakları mülakat botusun"})

def generate_response(prompt):
    st.session_state.messages.append({"role":"user","content": prompt})
    AI_response = client.chat.completions.create(
        model="gpt-4-1106-vision-preview",
        messages= st.session_state.messages,
        )
    return AI_response.choices[0].message.content

st.header("İlk Sohbet Botum")
st.divider()
for message in st.session_state.messages[1:]:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Mesajınızı Giriniz:"):
    st.chat_message("user").markdown(prompt)
    response = generate_response(prompt)
    with st.chat_message("assistant"):
        st.markdown(response)