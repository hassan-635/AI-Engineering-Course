

import re

text = """
Contact us at hassan@gmail.com,
support@yahoo.com,
admin@aiuk.edu.pk,
test.user123@outlook.com
"""

def mask_email(match):
    email = match.group()
    return ''.join('X' if ch != '@' else '@' for ch in email)

replaced_text = re.sub(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", mask_email, text)

print(replaced_text)