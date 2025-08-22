import streamlit as st
import time
import whisper
import tempfile

#ffmpeg
#openai-whisper
#toach

upload_file_kinds = [
    # テキスト系
    "txt","csv",

    # C / C++ 系
    ".c", ".cpp", ".cxx", ".cc", ".h", ".hpp", ".hh", ".m", ".mm",

    # Java 系
    ".java", ".kt", ".kts", ".scala",

    # Python 系
    ".py", ".pyw", ".pyc",

    # JavaScript / TypeScript 系
    ".js", ".mjs", ".ts", ".tsx", ".cjs",

    # Web系
    ".html", ".htm", ".css", ".scss", ".sass", ".json", ".xml",

    # スクリプト系
    ".sh", ".ps1", ".bat", ".pl", ".rb", ".php", ".lua",

    # データ / 設定系
    ".yml", ".yaml", ".toml", ".ini",

    # その他の言語
    ".go", ".rs", ".dart", ".swift", ".R", ".r", ".m", ".hs", ".jl", ".sql", ".asm", ".s",

    # Notebook
    ".ipynb"
]

st.markdown(
    """
    <style>
    .st-emotion-cache-18kf3ut {
        background-color: #add8e6;  /* 水色 */
        padding: 15px;              /* 内側の余白 */
        border-radius: 8px;         /* 角丸 */
        box-shadow: 0 8px 32px rgba(0,0,0,0.2);
    }
    .st-emotion-cache-zh2fnc {
        background: linear-gradient(135deg, #00bcd4 0%, #00acc1 100%);
        color: black;
        padding: 15px 40px;
        border: none;
        border-radius: 12px;
        font-size: 18px;
        font-weight: 600;
        cursor: pointer;
        box-shadow: 0 4px 15px rgba(0, 188, 212, 0.3);
        transition: transform 0.2s ease, box-shadow 0.2s ease;
        margin: 0 auto;
    }
    </style>
    """,
    unsafe_allow_html=True
)

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
        st.session_state.text = "Input some text here..."
    def add_text(new_text):
        st.session_state.text += "\n" + new_text  # 既存の文字列に追加
    def clear_text():
        st.session_state.text = ""

    def create_text_markdown(text):
        
        output_text =  f"""
                        <div style='
                            color: #000000;
                            padding: 30px;
                            font-size: 32px;
                            border-radius: 21px'>{text}
                        </div>
                        """
        st.markdown(output_text, unsafe_allow_html=True)
    # UIの構築
    st.title("レビュー構築メーカー(仮)")

    with st.container(border=False):
        create_text_markdown("・音声入力")
        _input_audio = st.audio_input("")
        if _input_audio is not None:    
            add_text(audio_trans_string(_input_audio))
            _input_audio = None  # 入力後はクリア
    with st.container(border=False):
        create_text_markdown("・*ここに気になった点を挙げてください")
        _input_text = st.text_area("",key="text")
        st.button("Clear", on_click=clear_text,)
    with st.container(border=False):
        create_text_markdown("・相手のレベルを選択してください")
        _select_level = st.selectbox("",["初学者", "中級者","上級者",])
    with st.container(border=False):
        st.markdown(
            """
            <style>
            /* ファイルタイプのドロップダウンを非表示にする */
            div[title="ファイルタイプを選択"] {
                display: none !important;
            }
            </style>
            """,
            unsafe_allow_html=True
        )
        create_text_markdown("・ファイルをアップロードしてください")
        _input_file = st.file_uploader("",type=upload_file_kinds,label_visibility = "collapsed")
    if st.button('送信'):
        if not _input_text:
            st.error("テキストを入力してください。")
        else:    
            return {"input_text":_input_text,"select_level":_select_level,"input_file":_input_file}

