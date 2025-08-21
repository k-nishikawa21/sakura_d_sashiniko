from google import genai
import os


def load_env_file():
    # あんまりよくないですが、環境変数を直接設定する方法
    # 後で変えると思います
    path = "sakura_d_sashiniko/secrets/secrets.txt"
    with open(path, "r") as f:
        content = f.read()
        os.environ["GEMINI_API_KEY"] = content
        

def make_response(prompt):
    load_env_file()
    client = genai.Client()
    response = client.models.generate_content(
        model="gemini-2.5-pro",
        contents=prompt
    )

    response_text = response.text

    # print(response.text)

    return response_text


if __name__ == "__main__":
    # __name__ == "__main__"で行われたものは，他のコードでimportして使われた際，反映されません
    # APIキーを含む環境変数ファイルのパス
    # envfile = "sakura_d_sashiniko/secrets/secrets.txt"
    prompt = "Hello, how are you today?"

    # ここでmake_responseを呼び出して，スポンスを取得
    response = make_response(prompt)
    print(response)
