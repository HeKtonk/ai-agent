import os
import argparse
from dotenv import load_dotenv
from google import genai
from google.genai import types
from prompts import system_prompt

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

def main():

    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")

    if api_key is None:
        raise RuntimeError("invalid api key")
    client = genai.Client(api_key=api_key)

    model = "gemini-2.5-flash"

    parser = argparse.ArgumentParser(description="Ai-chatbot")
    parser.add_argument("prompt", type=str, help="Write your prompt")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose outpout")
    args = parser.parse_args()

    messages = [types.Content(role="user", parts=[types.Part(text=args.prompt)])]
    conf = types.GenerateContentConfig(system_instruction=system_prompt)

    res = client.models.generate_content(model=model, contents=messages, config=conf)

    if res.usage_metadata is None:
        raise RuntimeError("failed api request, usage_metadata is None")
    if args.verbose:
        print(f"User prompt: {args.prompt}")
        print(f"Prompt tokens: {res.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {res.usage_metadata.candidates_token_count}")

    print(res.text)


if __name__ == "__main__":
    main()
