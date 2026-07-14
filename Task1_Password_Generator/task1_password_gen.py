import random
import string

def generate_password(length, use_letters=True, use_numbers=True, use_symbols=True):
    characters = ""
    if use_letters:
        characters += string.ascii_letters
    if use_numbers:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    if not characters:
        print("Please select at least one character type (Alphabetic, Numbers, or Symbols)!")
        return None

    password = "".join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("--- Auspify Password Generator ---")
    while True:
        try:
            length = int(input("\n give the lenght of password: "))
            if length <= 0:
                print("height more then 0")
                continue
            
            letters = input("Letters ? (y/n): ").lower() == 'y'
            numbers = input("Numbers include in? (y/n): ").lower() == 'y'
            symbols = input("Symbols include in? (y/n): ").lower() == 'y'

            password = generate_password(length, letters, numbers, symbols)
            if password:
                print(f"\nyour password is safe: {password}")
            
            repeat = input("\n Can you want to generate a new password? (y/n): ").lower()
            if repeat != 'y':
                print("Thankyou!")
                break
        except ValueError:
            print("pls put the right number")

if __name__ == "__main__":
    main()
