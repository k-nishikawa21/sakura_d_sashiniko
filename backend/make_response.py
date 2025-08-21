from google import genai
import os


def load_env_file(path):
    with open(path, "r") as f:
        content = f.read()
        os.environ["GEMINI_API_KEY"] = content
        

def make_response(prompt):
    client = genai.Client()
    response = client.models.generate_content(
        model="gemini-2.5-pro",
        contents=prompt
    )

    response_text = response.text

    # print(response.text)

    return response_text


if __name__ == "__main__":
    load_env_file("sakura_d_sashiniko/secrets/secrets.txt")
    prompt = "Hello, how are you today?"
    response = make_response(prompt)
    print(response)
