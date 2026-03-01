secret_number = 67
guess_count = 0
guess_limit = 3

while guess_count < guess_limit:
    try:
        guess = int(input('Guess the number: '))
        guess_count += 1
    except ValueError:
        print('Number must be an integer.')
        continue

    if guess == secret_number:
        print('Congratulations! You guessed the number!')
        break

    print(f'You have {guess_limit - guess_count} tries left')

else:
    print('You lost.')
