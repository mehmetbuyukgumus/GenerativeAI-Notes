import streamlit as st
import pandas as pd

st.header("Session State Mekanizması")

if "satir_sayisi" not in st.session_state:
    st.session_state.satir_sayisi = 10

data = pd.read_csv("/Users/mehmetbuyukgumus/Desktop/GenerativeAi-PromptEngineer/streamlit/data.csv", sep=",")

st.table(data.head(st.session_state.satir_sayisi))

def arttir():
    st.session_state.satir_sayisi += 1


def dusur():
    st.session_state.satir_sayisi -= 1


arttir_btn = st.button(label="Arttır👆🏻", on_click=arttir)
azalt_btn = st.button(label="Azalt👇🏻", on_click=dusur)


st.divider()
st.header(st.session_state.satir_sayisi)










# import streamlit as st

# st.session_state.mesaj = "Bilgilendirme Mesaji"
# st.session_state.yil = 2023
# st.session_state["Kullanıcı Adı"] = "Miuul"
# gunler = ["Pazartesi", "Salı", "Çarşamba", "Perşembe", "Cumar", "Cumartesi", "Pazar"]
# st.session_state.liste = gunler
# st.session_state.yil += 10
# st.session_state.eposta = st.text_input(label="Lütfen eposta adresinizi giriniz")
# st.text_input(label="Lütfen Şirenizi Giriniz", type="password", key="sifre")
# goruntule_btn = st.button(label="Görüntüle")

# if goruntule_btn:
#     st.info(st.session_state.eposta)
#     st.info(st.session_state.sifre)

# st.write(st.session_state)