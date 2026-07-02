
l = [1, 5, 128, 34,5]

g = l[0]

for i in range (1, len(l)):
    if l[i] > g:
        g = l[i]

print(f"Greatest number in list is : {g}")