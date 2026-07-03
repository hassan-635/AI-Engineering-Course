

list1 = ["apple", "banana", "mango"]
list2 = []

for words in list1:
    list2.insert(0, words)

print(list2)

list3 = list2[::-1]

print(list3)