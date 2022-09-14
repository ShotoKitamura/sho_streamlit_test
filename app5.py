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

##動画
#video_file = open("sz2.mp4", "rb")
#video_bytes = video_file.read()
#st.video(video_bytes)

#テキストボックス
name = st.text_input('名前')

#ボタン
submit_btn = st.button("送信")
cancel_btn = st.button("キャンセル")
#↑ボタンが押されている場合はtrue, 押されていない場合はfalse
print("submit_btn:{}".format(submit_btn))
print("cancel_btn:{}".format(cancel_btn))