import os

print("Current directory:", os.getcwd())

file_name = input("Enter file name: ").strip()

file_path = os.path.join(os.getcwd(), file_name)
# This combines the current directory and file name into one valid path.

print("Full path:", file_path)

print("Does file exist?", os.path.exists(file_path))
# This returns True if a file or directory exists at that path, and False otherwise.

def fileExistsOrNot(path):
        return os.path.exists(path)

if fileExistsOrNot(file_path):
     with open(file_path, "r") as file:
            read_file = file.read()
            print(read_file)
else:
    print("File Not Found")