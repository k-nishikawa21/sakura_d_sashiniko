import streamlit as st

def output(response_text):
    st.subheader('出力')
    output_text = f"""
    <div style='background-color: #ddeeff;
        color: #000000;
        padding: 10px;
        border-radius: 10px;
        white-space: pre-wrap'>{response_text}
    </div>
    """
    st.markdown(output_text, unsafe_allow_html = True)

if __name__ == "main":
    input_text = st.text_area('入力')
    output(input_text)