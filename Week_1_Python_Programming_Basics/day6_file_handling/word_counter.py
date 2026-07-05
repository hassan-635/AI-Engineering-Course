# create a program that counts number of occurences of a specific word in a text file

def read_file(filename):
    try:
        with open(filename, "r") as file:
            return file.read()
    except FileNotFoundError:
        return "File Not Found!!!"
    
def word_counter(content, word):
    count = 0
    words = content.split()
    for w in words:
        if w == word:
            count += 1
    return count

word = input("Please enter a word to search in file : ")
content = read_file("Week_1_Python_Programming_Basics/day6_file_handling/list_sample.txt")
repetition = word_counter(content, word)

if (repetition <= 0):
    print("Word Not Found!!!")
else:
    print(f"{word} found {repetition} times..")