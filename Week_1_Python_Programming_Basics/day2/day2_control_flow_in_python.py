# check if a number is prime

num = input("Enter a number: ")
num = int(num)

if num > 1:
    for i in range(2, num):
        if (num % i == 0):
            print(f"{num} is not a prime number")
            break
    else:
        print(f"{num} is a prime number")
        