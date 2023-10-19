import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

password_length = 12  # You can change this to your desired password length
generated_password = generate_password(password_length)

print("Generated Password:", generated_password)
