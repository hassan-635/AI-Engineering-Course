

def copy_content(filename):
    try:
        with open(filename, "r") as file:
            content = file.read()
            return content
    except FileNotFoundError:
        return "File Not found!!!"

def paste_content(filename, content):
    try:
        with open(filename, "w") as file:
            file.write(content)
    except FileNotFoundError:
        print("File Not found!!!")        

content = copy_content("Week_1_Python_Programming_Basics\day6_file_handling\list_sample.txt")
paste_content("Week_1_Python_Programming_Basics/day6_file_handling/new_file.txt", content)