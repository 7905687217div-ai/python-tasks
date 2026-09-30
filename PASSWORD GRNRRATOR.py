

import string
import random
# User input for password length
length = int(input("Enter password length: "))
# Character sets
letters = string.ascii_letters
digits = string.digits
special_chars = string.punctuation
# Combine all characters
all_chars = letters + digits + special_chars
# Generate password
password = ''.join(random.choice(all_chars) for _ in range(length))
print("Generated password:", password)

 