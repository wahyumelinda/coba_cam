import streamlit as st
from PIL import Image

st.title("Ambil Foto di Streamlit Cloud")

img_file = st.camera_input("Ambil gambar")

if img_file is not None:
    img = Image.open(img_file)
    st.image(img, caption="Hasil Foto")
