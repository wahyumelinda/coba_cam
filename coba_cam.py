import av
import cv2
import streamlit as st
from streamlit_webrtc import webrtc_streamer, VideoTransformerBase

st.title("Live Kamera dengan OpenCV + Streamlit")

# Bikin class untuk transformasi video frame
class VideoTransformer(VideoTransformerBase):
    def transform(self, frame):
        img = frame.to_ndarray(format="bgr24")

        # Contoh: ubah jadi grayscale
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        gray = cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)

        return gray

# Jalankan webrtc streamer
webrtc_streamer(key="example", video_transformer_factory=VideoTransformer)
