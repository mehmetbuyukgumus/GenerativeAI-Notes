import cohere
import os
from dotenv import load_dotenv

load_dotenv()

my_key = os.getenv("cohere_apikey")

client = cohere.Client(
    api_key=my_key
)

def generate_response(prompt):

    AI_Response = client.chat(
        model = "command",
        temperature=0,
        max_tokens=256,
        chat_history=[
            {"role": "USER", "message":"Yer çekimini kim bulmuştur?"},
            {"role": "CHATBOT", "message": "Çekim yasalarını formülize eden Sir Isaac Newton"}
        ],
        message=prompt
    )

    return AI_Response.text

import streamlit as st

st.header("Command ile İletişim Kurun")
st.divider()

prompt = st.text_input("Mesajınızı Giriniz:")
submit_btn = st.button("Gönder")

if submit_btn:
    response = generate_response(prompt)
    st.markdown(response)