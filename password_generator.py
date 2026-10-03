import random
import string

# Character groups
uppercase = string.ascii_uppercase
lowercase = string.ascii_lowercase
numbers = string.digits
symbols = string.punctuation


# Get password length
while True:
    try:
        length = int(input("Enter password length (minimum 8): "))

        if length < 8:
            print("Password length must be at least 8 characters.")
        else:
            break

    except ValueError:
        print("Please enter a valid number.")


# Choose character types
print("\nChoose the character types for your password.")
print("Enter yes or no.")

while True:

    use_uppercase = input("Include uppercase letters? (yes/no): ").lower()
    use_lowercase = input("Include lowercase letters? (yes/no): ").lower()
    use_numbers = input("Include numbers? (yes/no): ").lower()
    use_symbols = input("Include symbols? (yes/no): ").lower()

    choices = [use_uppercase, use_lowercase, use_numbers, use_symbols]

    # Check valid input
    if not all(choice in ["yes", "no"] for choice in choices):
        print("\nInvalid input! Please enter only yes or no.\n")
        continue

    # Check at least two types
    selected_count = choices.count("yes")

    if selected_count < 2:
        print("\nPlease select at least TWO character types.\n")
        continue

    break


# Create selected character groups
selected_groups = []

if use_uppercase == "yes":
    selected_groups.append(uppercase)

if use_lowercase == "yes":
    selected_groups.append(lowercase)

if use_numbers == "yes":
    selected_groups.append(numbers)

if use_symbols == "yes":
    selected_groups.append(symbols)


# Make sure every selected type appears at least once
password_characters = []

for group in selected_groups:
    password_characters.append(random.choice(group))


# Create remaining characters
all_characters = "".join(selected_groups)

remaining = length - len(password_characters)

for i in range(remaining):
    password_characters.append(random.choice(all_characters))


# Shuffle password
random.shuffle(password_characters)

password = "".join(password_characters)


# Display result
print("\n--------------------------------")
print("     RANDOM PASSWORD GENERATOR")
print("--------------------------------")
print("Generated Password:", password)
print("Password Length:", len(password))
print("--------------------------------")
