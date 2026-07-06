# write a program to log messages with timestamps into a file

from datetime import datetime as dt

def generate_log(message):
    return (message + " -> " +  str(dt.now().time()))

def write_log(filename, message):
    try:
        with open(filename, "a") as file:
            file.write(message + "\n") 
    except FileNotFoundError:
        print("File Not Found!!!")

def read_logs(filename):
    try:
        with open(filename, "r") as file:
            return file.read() 
    except FileNotFoundError:
        return "File Not Found!!!"

def start():
    loop = int(input("Please Enter total number of messages : "))
    while loop > 0:
        message = input(f"Enter Message : ")
        timed_log = generate_log(message)
        write_log("Week_1_Python_Programming_Basics\day6_file_handling\logs.txt", timed_log)
        loop -=1
    print("All logs : ")
    logs = read_logs("Week_1_Python_Programming_Basics\day6_file_handling\logs.txt")
    print(logs)

start()