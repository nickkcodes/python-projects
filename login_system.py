MAX_TRIES = 3
SPECIAL_CHARS = '!@#$%^&*()-_'

def login_system():
    tries = MAX_TRIES

    while tries > 0:
        user = input('Username: ')
        password = input('Password: ')
        age = get_age()

        errors = validate_credentials(user, password, age)

        if not errors:
            print('You are logged in! ')
            return

        tries -= 1

        if tries == 0:
            print('Account locked. ')
        else:
            for error in errors:
                print(error)
            else:
                print(f'You have {tries} tries left. ')

def get_age():
    while True:
        try:
            age = int(input('Age: '))
            return age
        except ValueError:
            print('Age must be a number. ')

def validate_credentials(user, password, age):
    errors = []

    if " " in user:
        errors.append('User cannot contain spaces. ')

    if " " in password:
        errors.append('Password cannot contain spaces. ')

    if len(user) < 8:
        errors.append('Username must be at least 8 characters long. ')

    if not any(char.isdigit() for char in user):
        errors.append('Username must have one digit. ')

    if not any(char.isupper() for char in user):
        errors.append('Username must have one uppercase letter. ')

    if len(password) < 8:
        errors.append('Password must at least 8 characters long. ')

    if not any(char.isdigit() for char in password):
        errors.append('Password must have one digit. ')

    if not any(char.isupper() for char in password):
        errors.append('Password must have one uppercase letter. ')

    if not any(char.islower() for char in password):
        errors.append('Password must have one lowercase letter. ')

    if not any(char in SPECIAL_CHARS for char in password):
        errors.append("Password must have one special characters [!@#$%^&*()-_] ")

    if age < 13:
        errors.append('You must be at least 13 years old to enter. ')

    return errors

login_system()
