from functions.run_python_file import run_python_file

result = run_python_file("calculator", "main.py")
print(f"Result for 'calculator/main.py' directory:\n{result}")
result = run_python_file("calculator", "main.py", ["3 + 5"])
print(f"Result for 'calculator/main.py' directory and ['3 + 5'] args :\n{result}")
result = run_python_file("calculator", "tests.py")
print(f"Result for 'calculator/tests.py' directory:\n{result}")
result = run_python_file("calculator", "../main.py")
print(f"Result for 'calculator/../main.py' directory:\n{result}")
result = run_python_file("calculator", "nonexistent.py")
print(f"Result for 'calculator/nonexistent.py' directory:\n{result}")
result = run_python_file("calculator", "lorem.txt")
print(f"Result for 'calculator/lorem.txt' directory:\n{result}")
