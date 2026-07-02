
try:
    num = int(input("Enter a number :"))
except ValueError:
    print(f"Please Enter a valid integer!!!")

if(num < 0):
    print("Please Enter a positive number")
else:
    result = 1
    for i in range(1, num+1):
        result *= i;

print(f"Factorial: {result}")