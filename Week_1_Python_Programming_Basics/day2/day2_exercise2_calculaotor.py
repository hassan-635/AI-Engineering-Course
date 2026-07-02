# menu driven calculator program

while True:
    
    try:
        num1 = float(input("Enter first number : "));
        num2 = float(input("Enter Second number : "));
    
    except ValueError:
        print("Error: Please enter generic number");
        continue;
    
    operation = input("Enter a character (/, *, +, -) : ");

    if(operation == "+"):
        output = num1 + num2;
    if(operation == "*"):
        output = num1 * num2;
    if(operation == "/"):
        if num2 == 0:
            print("Division by zero not Possible")
            continue;
        output = num1 / num2;
    if(operation == "-"):
        output = num1 - num2;
    else:
        print("Please Enter a valid operation")

    print(f"Result: {output}")
        
    while True:
        print(f"Presss 1 to continue and 0 to exit");
        choice = int(input());
        if(choice == 0):
            print(f"Exiting program")
            exit()
        elif (choice == 1):
            break;
        else:
            print("Please Enter a valid choice ( 0 or 1) : ");