# Importing necessary modules
import random
import string

# Greeting
print("🔐 Welcome to the Password Generator!")

# Asking the user for password configuration
password_length = int(input("🔢 Enter the total number of characters in the password:\n"))
num_letters = int(input("🔤 Enter the number of letters:\n"))
num_digits = int(input("🔢 Enter the number of digits:\n"))
num_symbols = int(input("🔣 Enter the number of symbols:\n"))

# Check if the total adds up
if password_length == (num_letters + num_digits + num_symbols):
    # Generating characters
    letters = random.choices(string.ascii_letters, k=num_letters)
    digits = random.choices(string.digits, k=num_digits)
    symbols = random.choices(string.punctuation, k=num_symbols)

    # Combine and shuffle
    password_chars = letters + digits + symbols
    random.shuffle(password_chars)

    # Join characters to form the final password
    final_password = ''.join(password_chars)

    print(f"\n✅ Your secure password is: {final_password}")
else:
    print("\n❌ Invalid input! The sum of letters, digits, and symbols must equal the total password length.")
