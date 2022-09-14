import streamlit as st
from PIL import Image

st.title("ショートアプリ")
st.caption("テストアプリです。")
st.subheader("コメント")
st.text("夏休みが終わって大変です。")
st.text("以下はサンプルプログラムです。")
code = '''
import streamlit as st

st.title("ショートアプリ")
'''
st.code(code, language='python')

#画像
image = Image.open("IMG_0010.PNG")
st.image(image, width = 200)

#動画
video_file = open("sz2.mp4", "rb")
video_bytes = video_file.read()
st.video(video_bytes)