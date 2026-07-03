

sentence = input("Please Enter a sentence :");

words_list = sentence.split()

words = {}

for word in words_list:
    word = word.lower();
    if word in words:
        words[word] += 1;
    else:
        words[word] = 1;

print(words)