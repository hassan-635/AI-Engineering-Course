
def check_palindrome(text):
    text2 = text[::-1]

    if text2 == text :
        return "palindrome"
    else:
        return "not palindrome"


text = "hassan ali abrar abrar ali hassan"
text2 = "a c a"

first = check_palindrome(text)
sec = check_palindrome(text2)

print(f"{text} is {first}")
print(f"{text2} is {sec}")