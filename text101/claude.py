import anthropic
import streamlit as st
import os
from dotenv import load_dotenv

load_dotenv()

my_key = os.getenv("claude_api_key")

client = anthropic.Anthropic(
    api_key=my_key
)

def generate_response(prompt):
    AI_Response = client.messages.create(
        model= "claude-2.1",
        temperature=0,
        max_tokens=256,
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
    return AI_Response.content.text[0]


st.header("Claude ile İletişim Kurun")
st.divider()

prompt = st.text_input("Mesajınızı Giriniz:")
submit_btn = st.button("Gönder")

if submit_btn:
    response = generate_response(prompt)
    st.markdown(response)