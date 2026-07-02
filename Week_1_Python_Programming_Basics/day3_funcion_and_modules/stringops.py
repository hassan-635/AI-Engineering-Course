

def rev(a):
    reversed_text = a[::-1];
    return reversed_text;

def vowel_count(a):
    vowels = "aeiou"
    count = 1;
    for char in a:
        for char in vowels:
            count+=1;
    return count

def palindrome_checker(a):
    if a == rev(a):
        return "you entered a palindrome string"
    else:
        return "you entered a non-palindrome string"
