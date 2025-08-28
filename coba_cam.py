import streamlit as st
import mediapipe as mp
import numpy as np
from PIL import Image, ImageDraw

st.title("Deteksi Wajah dengan Mediapipe")

img_file = st.camera_input("Ambil foto wajah")

if img_file is not None:
    image = Image.open(img_file).convert("RGB")
    img_array = np.array(image)

    # Inisialisasi mediapipe face detection
    mp_face_detection = mp.solutions.face_detection
    mp_drawing = mp.solutions.drawing_utils

    with mp_face_detection.FaceDetection(min_detection_confidence=0.5) as face_detection:
        results = face_detection.process(img_array)

        if not results.detections:
            st.warning("❌ Tidak ada wajah terdeteksi, coba foto lebih jelas / pencahayaan lebih terang")
        else:
            # Gambar kotak di wajah
            draw = ImageDraw.Draw(image)
            for detection in results.detections:
                bboxC = detection.location_data.relative_bounding_box
                ih, iw, _ = img_array.shape
                x, y, w, h = int(bboxC.xmin * iw), int(bboxC.ymin * ih), \
                             int(bboxC.width * iw), int(bboxC.height * ih)
                draw.rectangle([x, y, x + w, y + h], outline="green", width=3)

            st.image(image, caption="Hasil Deteksi Wajah")
