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

#フォームの形成
with st.form(key="profile_form"):
	#テキストボックス
	name = st.text_input('名前')

	#セレクトボックス
	age_category = st.selectbox("年齢層", ("未成年", "成人"))
	#age_category = st.radio("年齢層", ("未成年", "成人"))

	#ボタン
	submit_btn = st.form_submit_button("送信")
	cancel_btn = st.form_submit_button("キャンセル")
	if submit_btn == True:
		st.text("ようこそ！{}さん".format(name))
		st.text("年齢層：{}".format(age_category))