from functions.get_file_content import get_file_content

result = get_file_content("calculator","lorem.txt")
print(f"Result for 'calculator/lorem.txt' directory:\n{result}")
result = get_file_content("calculator","main.py")
print(f"Result for 'calculator/main.py' directory:\n{result}")
result = get_file_content("calculator","pkg/calculator.py")
print(f"Result for 'calculator/pkg/calculator.py' directory:\n{result}")
result = get_file_content("calculator","/bin/cat")
print(f"Result for '/bin/cat' directory:\n{result}")
result = get_file_content("calculator","pkg/does_not_exist.py")
print(f"Result for 'calculator/pkg/does_not_exist.py' directory:\n{result}")
