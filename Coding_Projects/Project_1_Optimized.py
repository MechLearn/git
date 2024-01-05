import random

def play_game():
    x = random.randint(1, 10)
    max_try = 10

    print(f'The random number is: {x}')

    for intento in range(1, max_try + 1):
        num = int(input(f'Attempt {intento}: Enter a number from 1 to 10: '))

        if num > 10:
            print("That option is not valid, please choose another number.")
        elif num == -1:
            print(f"Oh man, you used cheat codes! Well, the number is: {x}")
            break
        elif num == x:
            if intento == 1:
                print(f'Congratulations! You found the number in the first try!')
            else:
                print(f'Congratulations! You found the number in {intento} tries!')
            if input('Do you want to reset the game? (Y/N): ').lower() != 'y':
                return
        elif num > x:
            print('The number you selected is too high.')
            print(f"Attempts remaining: {max_try - intento}")
        elif num < x:
            print('The number you selected is too low.')
            print(f"Attempts remaining: {max_try - intento}")
        else:
            print('The number is not valid, please try again!')
            print(f"Attempts remaining: {max_try - intento}")

    print(f'Game over! The correct number was: {x}')
    if input('Do you want to reset the game? (Y/N): ').lower() != 'y':
        return

while True:
    play_game()
