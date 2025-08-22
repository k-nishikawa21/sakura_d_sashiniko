import frontend.input as finput
import frontend.output as foutput
import backend.make_prompt as bmake_prompt
import backend.make_response as bmake_response

def main():
    answer = finput.make_input_text()
    print(f"answer: {answer}")
    # 追加された生の文書の取得
    if answer is not None:
        input_text = answer["input_text"]
        print(f"input_text: {input_text}")
        prompt = bmake_prompt.make_prompt(input_text)
        print(f"prompt: {prompt}")
        answer = bmake_response.make_response(prompt)
        print(f"answer: {answer}")

        foutput.output(answer)

main()
