import os
from dotenv import load_dotenv
from google import genai

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

def main():
    print("Hello from ai-agent!")
     
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    if api_key is None:
        raise RuntimeError("invalid api key")
    client = genai.Client(api_key=api_key)

    model = "gemini-2.5-flash"
    prompt = "Why is Boot.dev such a great place to learn backend development? Use one paragraph maximum."

    res = client.models.generate_content(model=model, contents=prompt)
    print(res.text)


if __name__ == "__main__":
    main()
