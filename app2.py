import streamlit as st

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