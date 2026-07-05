

try:
    with open("Week_1_Python_Programming_Basics\day6_file_handling\sample.txt", "r") as file:
        content = file.read()
        character = len(content)
        words = len(content.split())
        lines = len(content.splitlines())

        print(f"Characters : {character}, Words : {words}, Lines : {lines}")
except FileNotFoundError:
    print("File Not Found")