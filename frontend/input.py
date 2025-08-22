import streamlit as st
import time
import whisper
import tempfile

#ffmpeg
#openai-whisper
#toach

def audio_trans_string(audio_bytes):
    # 一時ファイルに保存
    with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as f:
        f.write(audio_bytes.getbuffer())
        audio_path = f.name

    # Whisper モデルロード
    model = whisper.load_model("base")  # tiny / small / base / medium / large も可
    result = model.transcribe(audio_path, language="ja")  # 日本語で文字起こし
    return result["text"]

def make_input_text():
    #　テキストエリアに文字を追加するための初期化
    if "text" not in st.session_state:
        st.session_state.text = "ここに初期テキスト"
    def add_text(new_text):
        st.session_state.text += "\n" + new_text  # 既存の文字列に追加

    # UIの構築
    st.title("レビュー構築メーカー(仮)")

    _input_audio = st.audio_input('音声入力')
    if _input_audio is not None:    
        add_text(audio_trans_string(_input_audio))
    
    _input_text = st.text_area('ここに気になった点を挙げてください', key="text")
    _select_level = st.selectbox("相手のレベル", ["初学者", "中級者","上級者",])
    _input_file = st.file_uploader("Choose a file")
    if st.button('送信'):
        if not _input_text:
            st.error("テキストを入力してください。")
        else:    
            return {"input_text":_input_text,"select_level":_select_level,"input_file":_input_file}
    return None

make_input_text()