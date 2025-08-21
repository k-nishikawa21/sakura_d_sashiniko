import streamlit as st
import time


_input_text = st.text_area('ここに気になった点を挙げてください', 'Input some text here.')
_select_level = st.selectbox("相手のレベル", ["初学者", "中級者","上級者",])
_input_file = st.file_uploader("Choose a file")

def solve(input_text,Level,file):
    # 柔らかい文字に変換させる
    st.success("データの処理が完了しました！")
    return "処理結果"

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
            ans = solve(_input_text, _select_level, _input_file)