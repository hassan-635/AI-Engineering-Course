

def fact(num):
    if num < 0:
        return "Please Enter positive number"
    else:
        result = 1
        for i in range(1, num+1):
            result *= i
        return result
    
def caller():
    print(fact(-3));
    print(fact(0));
    print(fact(1));
    print(fact(5));


caller();