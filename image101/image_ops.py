from openai import OpenAI
import streamlit as st
from dotenv import load_dotenv
import os
import requests
from io import BytesIO
import base64

load_dotenv()

my_key_openai = os.getenv("openai_api_key")
my_key_stabilityai = os.getenv("stability_ai_api_key")

client = OpenAI(
    api_key=my_key_openai
)

def generate_images(prompt):
    AI_Response = client.images.generate(
        model= "dall-e-3",
        size = "1024x1024",
        quality="hd",
        n=1,
        response_format="url",
        prompt= prompt
    )
    image_url = AI_Response.data[0].url
    revised_prompt = AI_Response.data[0].revised_prompt
    response = requests.get(image_url)
    image_bytes = BytesIO(response.content)

    return image_bytes, revised_prompt


def generate_image_variation(source_img_url):
    AI_Response = client.images.create_variation(
        image=open(source_img_url, "rb"),
        size="1024x1024",
        n=1,
        response_format="url"
    )
    generated_image_url = AI_Response.data[0].url
    response = requests.get(generated_image_url)
    image_bytes = BytesIO(response.content)
    return image_bytes


def generate_with_SD(prompt):
    url = "https://api.stability.ai/v2beta/stable-image/generate/core"
    headers= {
        "Accept": "applicatin/json",
        "Content-type": "applicatin/json",
        "Authorization": f"Bearer {my_key_stabilityai}"
    }
    body = {
        "steps": 40,
        "widht": 1024,
        "height": 1024,
        "seed": 0,
        "cfg_scale": 5,
        "samples": 1,
        "text_prompts": [
            {
                "text": prompt,
                "weight": 1
            },
            {
                "text": "blurry, bad",
                "weight": -1
            }
        ],
    }
    response = requests.post(
        url,
        headers=headers,
        json=body
    )
    data = response.json()

    return data


tab_generate, tab_variation = st.tabs(["Resim Üret", "Varyasyon Oluştur"])

with tab_generate:
    st.subheader("DALL-E 3 ile Görsel Oluşturma")
    st.divider()
    prompt = st.text_input("Oluşturmak istediğiniz görseli tarif ediniz.")
    generate_btn = st.button(label="Oluştur")
    if generate_btn:
        image_data, reviesd_image = generate_images(prompt)
        st.image(image=image_data)
        st.divider()
        st.caption(reviesd_image)
        st.download_button(label="Download")

with tab_variation:
    st.subheader("DALL-E 3 ile Görsel Varyasyonu Oluşturma")
    st.divider()
    selecte_file = st.file_uploader("PNG formatinda bir görsel seçiniz", type=["png"])
    if selecte_file:
        st.image(image=selecte_file.name)
    variation_btn = st.button(label="Varyasyon Oluştur")