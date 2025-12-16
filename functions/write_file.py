import os

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
