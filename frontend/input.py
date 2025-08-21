import streamlit as st
import time



def make_input_text():
    _input_text = st.text_area('ここに気になった点を挙げてください', 'Input some text here.')
    _select_level = st.selectbox("相手のレベル", ["初学者", "中級者","上級者",])
    _input_file = st.file_uploader("Choose a file")
    if st.button('送信'):
        if not _input_text:
            st.error("テキストを入力してください。")
        elif not _select_level:
            st.error("レベルを選択してください。")
        elif _input_file is None:
            st.error("ファイルをアップロードしてください。")
        else:
            with st.spinner("データを処理中です..."):
                time.sleep(2)  #　
                return {"input_text":_input_text,"select_level":_select_level,"input_file":_input_file}

    return {"input_text":None,"select_level":None,"input_file":None}