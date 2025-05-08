import random
import string

def generate_password(length=12, use_upper=True, use_digits=True, use_symbols=True):
    # Start with lowercase letters
    characters = string.ascii_lowercase
    
    if use_upper:
        characters += string.ascii_uppercase
    if use_digits:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    if not characters:
        raise ValueError("No character types selected!")

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Ask the user for their preferences
try:
    length = int(input("Enter desired password length: "))
    use_upper = input("Include uppercase letters? (y/n): ").lower() == 'y'
    use_digits = input("Include digits? (y/n): ").lower() == 'y'
    use_symbols = input("Include symbols? (y/n): ").lower() == 'y'

    password = generate_password(length, use_upper, use_digits, use_symbols)
    print(f"\nGenerated Password: {password}")
except ValueError:
    print("Please enter a valid number.")