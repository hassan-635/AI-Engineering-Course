

try:
    with open("Week_1_Python_Programming_Basics\day6_file_handling\sample.txt", "r") as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("File not found!!!")