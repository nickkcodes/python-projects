# Login System

MAX_TRIES = 3
SPECIAL_CHARS = "!@#$%^&*()-_+="

tries = MAX_TRIES

while tries > 0:
    user = input('Username: ')
    password = input('Password: ')

    # Handle invalid age input
    try:
        age = int(input('Age: '))
    except ValueError:
        print("Age must be a number.")
        tries -= 1
        if tries > 0:
            print(f"Wrong input. You have {tries} tries left.\n")
        else:
            print("Account locked.")
        continue

    valid = True  # reset for this attempt

    # Username rules
    if len(user) < 5:
        print('Username must be at least 5 characters.')
        valid = False

    if not any(char.isupper() for char in user):
        print('Username must contain at least one uppercase letter.')
        valid = False

    # Password rules
    if len(password) < 8:
        print('Password must be at least 8 characters.')
        valid = False

    if sum(char.isdigit() for char in password) < 2:
        print('Password must contain at least 2 numbers.')
        valid = False

    if not any(char.isupper() for char in password):
        print('Password must contain at least one uppercase letter.')
        valid = False

    if not any(char.islower() for char in password):
        print('Password must contain at least one lowercase letter.')
        valid = False

    if not any(char in SPECIAL_CHARS for char in password):
        print(f'Password must contain at least one special character: {SPECIAL_CHARS}')
        valid = False

    # Age rule
    if age < 13:
        print('You must be at least 13 years old.')
        valid = False

    # Check final result
    if valid:
        print("\nAccess granted ✅")
        break
    else:
        tries -= 1
        if tries > 0:
            print(f"\nInvalid credentials. You have {tries} tries left.\n")
        else:
            print("\nAccount locked ❌")
