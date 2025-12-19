import os
from google import genai
from google.genai import types

def write_file(working_directory,file_path,content):

    target_dir_abs_path = os.path.abspath(os.path.join(working_directory, file_path))
    working_directory_abs_path = os.path.abspath(working_directory)
    if not target_dir_abs_path.startswith(working_directory_abs_path):
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
    file_index = target_dir_abs_path.rfind('/')
    try:
        if not os.path.exists(target_dir_abs_path[:file_index]):
            os.makedirs(target_dir_abs_path[:file_index])
    except Exception as e:
        return f"Error: {e}"

    with open(target_dir_abs_path, 'w') as f:
        f.write(content)
    return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'

schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description=(
        "Write or overwrite files at the specified filepath,"
        "constrained to the working directory."
    ),
    parameters=types.Schema(
        type=types.Type.OBJECT,
        required=["file_path", "contents"],
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description=(
                    "The path of the file to be written, relative to the working "
                    "directory. Use '.' for the working directory itself."
                ),
            ),
            "contents": types.Schema(
                type=types.Type.STRING,
                    description=(
                    "Contents to be written in the file"
                ),
            ),
        },
    ),
)
