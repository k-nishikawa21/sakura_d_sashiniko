import frontend.input as finput
import frontend.output as foutput
import backend.make_prompt as bmake_prompt
import backend.make_response as bmake_response
import streamlit as st
import concurrent.futures
def main():
    answer = finput.make_input_text()
    print(f"answer: {answer}")
    # 追加された生の文書の取得
    if answer is not None:
        with st.spinner("処理中です..."):
            input_text = answer["input_text"]
            print(f"input_text: {input_text}")
            prompt = bmake_prompt.make_final_prompt(input_text, answer["input_file"])
            print(f"prompt: {prompt}")
            with concurrent.futures.ThreadPoolExecutor(max_workers=1) as executor:
                future = executor.submit(bmake_response.make_response, prompt)
                try:
                    # 5秒間で終わらなければ例外を投げる
                    answer = future.result(timeout=5)
                except concurrent.futures.TimeoutError:
                    placeholder = st.empty()
                    with placeholder.container():
                        st.write("もう少しお待ちください...")
                    answer = future.result()
                    placeholder.empty()
            print(f"answer: {answer}")
        foutput.output(answer)
main()