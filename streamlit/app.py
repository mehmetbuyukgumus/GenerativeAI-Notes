import streamlit as st
import json

# Streamlit Uygulamasının başlatılması
# st.write("Hello World")

# Streamlit Sayfa Bilgilerini Düzenleme
st.set_page_config(page_title="Streamlit 101", page_icon=u"\U0001F916")

# # Streamlit İle Metin Gösterme
# --------------------------------------------------------
# st.write("Lorem ipsilum") # Metin yazdırma
# st.markdown("_Bu bir metindir_") # 
# st.header("Bu bir header örneği")
# st.subheader("Bu bir subheader örneği")
# st.code('for i in range(10): my_function')
# st.latex("e + 1 * 3")

# # Streamlit İle Multimedya Gösterme
# --------------------------------------------------------
# st.image(image="streamlit/1-image_sample.png") # Resim gösterme
# st.video(data='streamlit/2-video_sample.mp4') # Video gösterme
# st.audio(data="streamlit/speech.mp3") # Ses dosyası gösterme

# # Streamlit İle Kullanıcı Etkileşimi
# --------------------------------------------------------
# st.write("Lütfen Bilgilerinizi Giriniz")
# st.text_input(label="Lütfen e-posta adresinizi giriniz")
# st.text_input(label="Lütfen şifrenizi adresinizi giriniz", type="password")
# st.checkbox(label="Şifremi Unuttum")
# st.divider()
# st.number_input(label="Lütfen Yaşınızı Giriniz", min_value=18, max_value=40)
# st.slider(label="Lütfen Yaşınızı Giriniz", min_value=18, max_value=40, value=22)
# st.divider()
# st.radio(label="Statünüz nedir?", options=["Öğrenci", "Mezun"])
# st.button(label="Giriş Yap")
# st.file_uploader(label="Lütfen Dosyanızı Seçin")

# # Streamlit İle Arayüz Tasarımı (col, tab, slider)
# --------------------------------------------------------
# col1, col2 = st.columns(2)
# with col1:
#     st.markdown("""
# <h3><b> Kullanıcı bilgileri </b> </h3>
# """, unsafe_allow_html=True)
#     st.text_input(label="E-posta adresinizi giriniz")
#     st.text_input(label="Paorılanızı giriniz", type="password")
#     st.checkbox("Şifremi Unuttum")
#     st.divider()
#     st.button("Giriş Yap")

# with col2:
#         st.markdown("""
# <h3><b> Kullanıcı Tercihleri </b> </h3>
# """, unsafe_allow_html=True)
#         st.radio("Statünüzü Giriniz:", options=["Öğrenci", "Mezun"])
#         st.slider("Zaman Aşımı Süresi", min_value=18, max_value=40, value=5)
#         st.file_uploader("Güncel CV'nizi yükleyiniz")

st.sidebar.markdown("<h4>Hoşgeldiniz</h4>", unsafe_allow_html=True)
st.sidebar.image("streamlit/1-image_sample.png")

tab1, tab2 = st.tabs(["Kullanıcı bilgileri", "Kullanıcı Terichleri"])
with tab1:
    eposta = st.text_input(label="E-posta adresinizi giriniz")
    parola = st.text_input(label="Paorılanızı giriniz", type="password")
    st.checkbox("Şifremi Unuttum")
    st.divider()
    kaydet_btn = st.button("Giriş Yap")

with tab2:
    hesap_turu = st.radio("Statünüzü Giriniz:", options=["Öğrenci", "Mezun"])
    st.slider("Zaman Aşımı Süresi", min_value=18, max_value=40, value=5)
    st.file_uploader("Güncel CV'nizi yükleyiniz")

if kaydet_btn:
    data = []
    data.append({"eposta": eposta})
    data.append({"password": parola})

    if hesap_turu == "Öğrenci":
        gecerlilik_suresi = 365
    elif hesap_turu == "Mezun":
        gecerlilik_suresi = 30

    data.append({"Geçerlilik Süresi": gecerlilik_suresi})

    with open("kullanici.txt", "w") as file:
        file.write(json.dumps(data))
    
    st.balloons()
    st.success("Dosyanız Kaydedildi")
    st.write(f"Belirlenen Geçerlilik Süresi: {gecerlilik_suresi}")

