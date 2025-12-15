import os

def get_files_info(working_directory, directory="."):

    target_dir_abs_path = os.path.abspath(os.path.join(working_directory, directory))
    working_directory_abs_path = os.path.abspath(working_directory)
    if not target_dir_abs_path.startswith(working_directory_abs_path):
        return f'    Error: Cannot list "{directory}" as it is outside the permitted working directory'
    elif os.path.isfile(target_dir_abs_path):
        return f'    Error: "{directory}" is not a directory'

    files_in_dir = os.listdir(target_dir_abs_path)
    result = []

    for file in files_in_dir:
        file_path = f"{target_dir_abs_path}/{file}"
        result.append(f"  - {file}: file_size={os.path.getsize(file_path)}, is_dir={os.path.isdir(file_path)}")
    return '\n'.join(result)
