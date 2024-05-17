import random
import string

def create_password(length, letters=True, numbers=True, special_chars=True):
    char_set = ''
    if letters:
        char_set += string.ascii_letters
    if numbers:
        char_set += string.digits
    if special_chars:
        char_set += string.punctuation

    if not char_set:
        print("Error: You must select at least one character type.")
        return None

    generated_password = ''.join(random.choice(char_set) for _ in range(length))
    return generated_password

def password_generator():
    print("Password Generator")

    password_length = int(input("Enter password length: "))
    include_letters = input("Include letters? (y/n): ").lower() == 'y'
    include_numbers = input("Include numbers? (y/n): ").lower() == 'y'
    include_special_chars = input("Include special characters? (y/n): ").lower() == 'y'

    generated_password = create_password(password_length, include_letters, include_numbers, include_special_chars)
    if generated_password:
        print("Generated password:", generated_password)

if __name__ == "__main__":
    password_generator()
