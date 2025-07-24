# Password Generator Tool - CodSoft Internship Task 2
import random
import string

def generate_password(length):
    """
    Generates a secure password using uppercase, lowercase, digits, and symbols.
    
    Parameters:
        length (int): Desired length of the password.
    
    Returns:
        str: Randomly generated password.
    """
    if length < 4:
        return "Password length should be at least 4 characters for a secure password."

    # Define character sets
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    symbols = string.punctuation

    # Combine all characters
    all_chars = lowercase + uppercase + digits + symbols

    # Ensure the password has at least one of each type
    password = [
        random.choice(lowercase),
        random.choice(uppercase),
        random.choice(digits),
        random.choice(symbols)
    ]

    # Fill the remaining length
    password += random.choices(all_chars, k=length - 4)

    # Shuffle to avoid predictable pattern
    random.shuffle(password)

    return ''.join(password)

def main():
    print("🔐 Welcome to the Password Generator 🔐")
    try:
        length = int(input("Enter desired password length: "))
        password = generate_password(length)
        print(f"\nYour generated password is:\n👉 {password}")
    except ValueError:
        print("❌ Please enter a valid number.")

if __name__ == "__main__":
    main()
