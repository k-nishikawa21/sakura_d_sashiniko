import frontend.input as finput
import frontend.output as foutput
import backend.make_prompt as bmake_prompt
import backend.make_response as bmake_response

def main():
    answer = finput.make_input_text()
    # 追加された生の文書の取得
    input_text = answer["input_text"]
    prompt = bmake_prompt.make_prompt(input_text)
    answer = bmake_response.make_response(prompt)

    foutput.output(answer)

main()
