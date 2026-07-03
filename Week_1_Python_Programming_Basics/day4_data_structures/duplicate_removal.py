
numbers = [1, 2, 3, 2, 4, 5, 1, 6, 4, 7]

num = set(numbers)

unique = []

for n in numbers:
    if numbers.count(n) ==1:
        unique.append(n)

print(numbers)
print(num)
print(unique)

unique.sort()
print(unique)

unique.sort(reverse=True)
print(unique)