import os
import subprocess

def run_python_file(working_directory, file_path, args=[]):

    target_dir_abs_path = os.path.abspath(os.path.join(working_directory, file_path))
    working_directory_abs_path = os.path.abspath(working_directory)
    if not target_dir_abs_path.startswith(working_directory_abs_path):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    if not os.path.exists(target_dir_abs_path):
        return f'Error: File "{file_path}" not found.'
    if not file_path.endswith('.py'):
        return f'Error: "{file_path}" is not a Python file.'

    try:
        complete_process = subprocess.run(["python3", target_dir_abs_path, *args], cwd=working_directory_abs_path, capture_output=True, text=True, timeout=30)
    except Exception as e:
        return f"Error: executing Python file: {e}"

    if not complete_process.stdout and not complete_process.stderr:
        return "No output produced"

    result = f"STDOUT:\n{complete_process.stdout}\nSTDERR:\n{complete_process.stderr}"
    if complete_process.returncode != 0:
        result += f"\nProcess exited with code {complete_process.returncode}"

    return result

