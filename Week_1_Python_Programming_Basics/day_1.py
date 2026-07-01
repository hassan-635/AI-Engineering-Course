# write a message
name = input("Please enter your name: ")
print(f"Hello, {name}! Welcome to Python programming!")

# varibales creation of different data types
age = 25;
marks = 85.5;
string = "hi hassan"
list = [1, 2, 3, 4, 5]
tuple_var = (1, 2, 3, 4, 5)
dict_var = {"name": "hassan",
            "age": 25,
            "marks": 85.5};
boolean_var = True

#print and manipulate vars

print(f"Name: {name}, Age: {age}, Marks: {marks}")
print(f"List: {list}")
print(f"Tuple: {tuple_var}")
print(f"Dictionary: {dict_var}")
print(f"Boolean: {boolean_var}")

print(f"{string} + how are you?")
list.append(6)
print(f"Updated List: {list}")

print(f"name is : {dict_var['name']}")
