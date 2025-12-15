from functions.get_files_info import get_files_info

for_current_dir = get_files_info("calculator", ".")
print(f"Result for current directory:\n{for_current_dir}")
for_pkg_dir = get_files_info("calculator", "pkg")
print(f"Result for 'pkg' directory:\n{for_pkg_dir}")
for_bin_dir = get_files_info("calculator", "/bin")
print(f"Result for '/bin' directory:\n{for_bin_dir}")
for_dotdot_dir = get_files_info("calculator", "../")
print(f"Result for '../' directory:\n{for_dotdot_dir}")
