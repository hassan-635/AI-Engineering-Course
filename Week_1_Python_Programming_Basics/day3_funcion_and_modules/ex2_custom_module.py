from mymath import addition as a
from mymath import multiplication as m
from mymath import division as d
from mymath import subtraction as s

n1 = int(input("Enter first number : "));
n2 = int(input("Enter Second number : "));

print(f"Addition : {a(n1, n2)}")
print(f"Multiplication : {m(n1, n2)}")
print(f"Division : {d(n1, n2)}")
print(f"Subtraction : {s(n1, n2)}")