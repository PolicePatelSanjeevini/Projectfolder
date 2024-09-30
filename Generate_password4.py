
import random
import string
import pyperclip
#define characters
def generate_password(length, use_uppercase, use_symbols, use_numbers):
    lowercase_letters=string.ascii_lowercase
    uppercase_letters=string.ascii_uppercase
    numbers= string.digits if use_numbers else ''
    symbols=string.punctuation if use_symbols else ''

    all_characters=lowercase_letters + uppercase_letters + numbers + symbols 
    if not all_characters:
        print("Error: No character type selected.Please select a valid chaacter")
        return None

    # Generate password
    password = ''.join(random.choice(all_characters) for _ in range(length))
    return password


def main():
    print("Welcome to the Random password generator!")
    length=int(input("Enter the desired length of the password: "))
    uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
    Symbols= input("Include symbols? (y/n): ").lower() == 'y'
    numbers = input("Include numbers? (y/n): ").lower() == 'y'

    password = generate_password(length, uppercase, numbers, Symbols)
    
    if password:
        print(f"\nGenerated Password: {password}")

    

    copy_to_clipboard = input("Copy the password to clipboard? (y/n): ")
    if copy_to_clipboard == 'y':
        pyperclip.copy(password)
        print("Password copied to clipboard.")

if __name__ == "__main__":
    main()





    
    


