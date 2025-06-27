import random
import string

print("🔐 Password Generator")

try:
    length = int(input("Enter desired password length (e.g. 12): "))
    if length <= 0:
        raise ValueError("Length must be positive.")
except ValueError:
    print("❌ Invalid length. Please enter a positive integer.")
    input("Press Enter to exit...")
    exit()

digits_choice = input("Include digits? (y/n): ").strip().lower()
symbols_choice = input("Include symbols? (y/n): ").strip().lower()

# Базовый алфавит: буквы
characters = list(string.ascii_letters)

if digits_choice == 'y':
    characters += list(string.digits)

if symbols_choice == 'y':
    characters += list("!@#$%^&*()_+-=[]{}|;:,.<>?")

if not characters:
    print("❌ No characters selected for password.")
    input("Press Enter to exit...")
    exit()

# Генерация пароля
password = ''.join(random.choice(characters) for _ in range(length))

print("\n✅ Your generated password:")
print(password)

input("\nPress Enter to exit...")
