# This is a guess the number game.

import random
secretNumber = random.randint(1,9)
print('I am thinking of a number between 1 and 9.')

# Ask the player to guess 4 times.
for guessesTaken in range(1,5):
    print('Take a guess.')
    guess = int(input())

    if guess < secretNumber:
        print('Your guess is too low.')
    elif guess > secretNumber:
        print('Your guess is too high.')
    else:
        break # This condition is the correct guess!

if guess == secretNumber:
    print('\n Good job! You guessed the correct number in ' + str(guessesTaken) + ' guesses')
else:
    print('Nope. The number I was thinking of was ' + str(secretNumber) )
    

# Different variation of the same game.
attempts = 4
secNum = random.randint(1,9)
print('\n New game!')
for attempt in range(attempts, 0, -1):
    print("You have {0} attempts left.".format(attempt))
    number = int(input())
    if number < secNum:
        print('Your guess is too low.')
    elif number > secNum:
        print('Your guess is too high.')
    else:
        if number == secNum:
            print('Good job! You guessed the correct number in ' + str(attempts-attempt+1) + ' attempts.')
        else:
            print('Nope. The number I was thinking of was ' + str(secNum) )
        break
else:
    print('You''re out of guesses')
