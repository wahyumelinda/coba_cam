import streamlit as st
import cv2
import numpy as np
from PIL import Image

st.title("Deteksi Wajah dengan Kotak")

# Ambil foto dari kamera
img_file = st.camera_input("Ambil foto wajah")

if img_file is not None:
    # Buka gambar
    image = Image.open(img_file)
    img = np.array(image)

    # Convert ke grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Load model deteksi wajah Haar Cascade
    face_cascade = cv2.CascadeClassifier(
        cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
    )

    # Deteksi wajah (hasil berupa list kotak (x,y,w,h))
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

    # Gambar kotak hijau di wajah yang terdeteksi
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3)

    # Kalau tidak ada wajah terdeteksi
    if len(faces) == 0:
        st.warning("❌ Tidak ada wajah terdeteksi, coba foto lebih jelas / pencahayaan lebih terang")

    # Tampilkan hasil
    st.image(img, caption="Hasil Deteksi Wajah", channels="BGR")
