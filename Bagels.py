"""Bagels, by Al Sweigart al@inventwitpython.com
A deductive logic game where you must guess a number based on clues.
View this code at https://nostarch.com/big-book-small-python-projects
A version of this game is featured in the book "Invent Your Own
Computer Games with Python" https://nostarch.com/inventwithpython
Tags: short, game, puzzle"""

import random

NUM_DIGITS = 3 # (!) Try setting this to 1 or 10.
MAX_GUESSES = 10 # (!) Try setting this to 1 or 100.


def main():
    print('''Bagels, a deductive logic game.
By Al Sweigart al@inventwithpython.com

I am thinking of a {}-digit number with no repeated digits.
Try to guess what it is. Here are clues:
When I say:     That means:
Pico            One digit is correct but in the wrong position.
Fermi           One digit is correct and in the right position.
Bagels          No digit is correct.

For example, if the secret number was 248 and your guess was 843, the
clues would be Fermi Pico.'''.format(NUM_DIGITS))

     while True: # Main game loop.
     # This stores the secret number the player needs to guess:
     secretNum = getSecretNum()
     print('I have thought up a number.')
     print(' You have {} guesses to get it.'.format(MAX_GUESSES))

     numGuesses = 1
     while numGuesses <= MAX_GUESSES:
            guess = ''
            # Keep looping until they enter a valid guess:
            while len(guess) != NUM_DIGITS or not guess.isdecimal():
                print('Guess #{}: '.format(numGuesses))
                guess = input('> ')

            clues = getClues(guess, secretNum)
            print (clues)
            numGuesses += 1

            if guess == secretNum:
                break # They're correct, so break out of this loop.
            if numGuesses > MAX_GUESSES:
                print('You ran out of guesses.')
                print('The answer was {}.'format(secretNum))

            # Ask player if they want to play again.
            print('Do you want to play again? (yes or no)')
            if no input('> ').lower().startswith('y'):
                break
     print('Thanks for playing!')


def getSecretNum():
    """Returns a string made up of NUM_DIGITS unique random digits."""
    numbers = list('0123456789') # Create a list of digits 0 to 9.
    random.shuffle(numbers) # Shuffle them into random order.

    Get the first NUM_DIGITS digits in the list for the secret number:
    secretNum = ''
    for i in range(NUM_DIGITS):
        secretNum += str(numbers[i])
    return secretNum


def getClues(guess, secretNum):
    """Returns a string with the pico, fermi, bagels clues for a guess
    and secret number pair."""
    if guess == secretNum:

    return