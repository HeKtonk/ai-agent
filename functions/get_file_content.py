import os
from google import genai
from google.genai import types
from functions.config import MAX_CHARS

def get_file_content(working_directory, file_path):

    target_dir_abs_path = os.path.abspath(os.path.join(working_directory, file_path))
    working_directory_abs_path = os.path.abspath(working_directory)
    
    if not target_dir_abs_path.startswith(working_directory_abs_path):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    elif not os.path.isfile(target_dir_abs_path):
        return f'Error: File not found or is not a regular file: "{file_path}"'
    
    try:
        with open(target_dir_abs_path, 'r') as f:
            file_content_string = f.read(MAX_CHARS)
        if os.path.getsize(target_dir_abs_path) > MAX_CHARS:
            file_content_string = f'{file_content_string}[...File "{file_path}" truncated at 10000 characters]'
        return file_content_string
    except Exception as e:
        return f"Error: {e}"

schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description=(
        "Read files contents in the specified directory, "
        "constrained to the working directory."
    ),
    parameters=types.Schema(
        type=types.Type.OBJECT,
        required=["file_path"],
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description=(
                    "The filepath to list files from, relative to the working "
                    "directory. Use '.' for the working directory itself."
                ),
            ),
        },
    ),
)
