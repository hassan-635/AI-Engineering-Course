from functools import reduce


add = lambda x, y: (x+y)
print(add(3, 5))


num = [1, 2, 3, 4]
squares = map(lambda x: x**2, num)
print(list(squares))


even = filter(lambda x: x%2 == 0, num)
print(list(even))


product = reduce(lambda x, y: x*y, num)
print(product)