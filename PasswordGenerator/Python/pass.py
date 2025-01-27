from string import ascii_letters, digits, punctuation
from random import choices
import re

inp = input("Enter the length of the password: ")
c = ascii_letters + digits + punctuation
password = ''.join(choices(c, k=int(inp)))

for i in password:
    if re.search('[a-z]', i):
        if re.search('[A-Z]', i):
            if re.search('[0-9]', i):
                if re.search('[' + punctuation + ']', i):
                    print(password)
                    break

print("Password generated successfully!")
print("Password:", password)

if len(password) < 8:
    print("Password is weak!")
elif len(password) < 12:
    print("Password is moderate!")
else:
    print("Password is strong!")