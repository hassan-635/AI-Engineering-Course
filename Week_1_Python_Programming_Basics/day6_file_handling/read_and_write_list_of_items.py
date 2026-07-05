

def readFile(filename):
    try:
        with open(filename, "r") as file:
            content = file.read().splitlines()
            print(content)
    except FileNotFoundError:
        print("File not found !!!")

def writeFile(filename):
    try:
        with open(filename, "w") as file:
            content = ["pakistan", "iraq", "iran", "oman", "turkey"]
            for items in content:
                file.write(items + "\n")
    except FileNotFoundError:
        print("File Not Found !!!")

readFile("Week_1_Python_Programming_Basics\day6_file_handling\list_sample.txt")
writeFile("Week_1_Python_Programming_Basics\day6_file_handling\list_sample.txt")