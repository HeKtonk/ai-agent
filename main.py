import os
import argparse
from dotenv import load_dotenv
from google import genai

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

def main():

    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")

    if api_key is None:
        raise RuntimeError("invalid api key")
    client = genai.Client(api_key=api_key)

    model = "gemini-2.5-flash"
    prompt = "Why is Boot.dev such a great place to learn backend development? Use one paragraph maximum."

    parser = argparse.ArgumentParser(description="Ai-chatbot")
    parser.add_argument("prompt", type=str, help="Write your prompt")
    args = parser.parse_args()

    res = client.models.generate_content(model=model, contents=args.prompt)


    if res.usage_metadata is None:
        raise RuntimeError("failed api request, usage_metadata is None")
    print(f"Prompt tokens: {res.usage_metadata.prompt_token_count}")
    print(f"Response tokens: {res.usage_metadata.candidates_token_count}")

    print(res.text)


if __name__ == "__main__":
    main()
