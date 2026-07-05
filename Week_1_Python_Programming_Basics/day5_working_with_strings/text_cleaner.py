import re

text = "hassan , (a healthy boy) who was         once, roaming in the jumngle; he found a treasure there and also find \"gold stamp\". This gold stamp was very beautiful;."

cleaned = re.sub(r"[^\w\s]", "", text)
cleaned_text = " ".join(cleaned.split())

print(cleaned_text)