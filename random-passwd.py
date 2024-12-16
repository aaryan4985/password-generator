import random
import string

def generate_password(length, use_uppercase=True, use_numbers=True, use_special=True):
    
    characters = string.ascii_lowercase
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_numbers:
        characters += string.digits
    if use_special:
        characters += string.punctuation
    
    
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("🔒 Random Password Generator 🔒\n")
    
    
    length = int(input("Enter the password length: "))
    use_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
    use_numbers = input("Include numbers? (y/n): ").lower() == 'y'
    use_special = input("Include special characters? (y/n): ").lower() == 'y'
    
    
    password = generate_password(length, use_uppercase, use_numbers, use_special)
    print(f"\nYour generated password: {password}")
    
    
    while input("\nGenerate another password? (y/n): ").lower() == 'y':
        password = generate_password(length, use_uppercase, use_numbers, use_special)
        print(f"\nYour new password: {password}")

if __name__ == "__main__":
    main()
