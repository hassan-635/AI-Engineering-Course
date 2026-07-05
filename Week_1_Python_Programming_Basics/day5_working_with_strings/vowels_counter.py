text = "hassan ali abrar is an AI engineer"

vowels = "aeiouAEIOU"
count = 0;

for char in text:
    if char in vowels:
        count += 1


print(f"Vowels : {count}")