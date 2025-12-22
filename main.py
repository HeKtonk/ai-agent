import os
import argparse
from dotenv import load_dotenv
from google import genai
from google.genai import types
from prompts import system_prompt
from functions.get_files_info import schema_get_files_info
from functions.get_file_content import schema_get_file_content
from functions.write_file import schema_write_file
from functions.run_python_file import schema_run_python_file
from functions.call_function import call_function

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
    available_functions = types.Tool(function_declarations=[
        schema_get_files_info,
        schema_get_file_content,
        schema_write_file,
        schema_run_python_file
    ])
    conf = types.GenerateContentConfig(tools=[available_functions],system_instruction=system_prompt)


    res = client.models.generate_content(model=model, contents=messages, config=conf)

    if res.usage_metadata is None:
        raise RuntimeError("failed api request, usage_metadata is None")
    if args.verbose:
        print(f"User prompt: {args.prompt}")
        print(f"Prompt tokens: {res.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {res.usage_metadata.candidates_token_count}")

    function_call_responses = []
    print(res.text)
    if res.function_calls and (res.function_calls is not None):
        for fc in res.function_calls:
            print(f"Calling function: {fc.name}({fc.args})")
            function_call_result = call_function(fc)

            part = function_call_result.parts[0]

            if not part.function_response or not part.function_response.response:
                raise Exception("Fatal exception")

            function_call_responses.append(part)

            if args.verbose:
                print(f"-> {part.function_response.response}")


if __name__ == "__main__":
    main()
