#--------------------------------
#
# Student Name:Lucas Antonsen
# Student Number:
# Assignment 2: letter guessing game
#
# Date Created:Oct. 3/17
# Python Version: 3.6.2
#--------------------------------

import os
import sys
import random
import string

def guessing_game(computer_letter):
    
    lower_bound = 'A'
    upper_bound = 'Z'
    guesses = 1
    
    while True:
        
        question = lower_bound + ' - ' + upper_bound + ' (guess #' + str(guesses) + '): '
        guessed_letter = input(question).upper()

        #invalid type/outside of range
        if guessed_letter <= lower_bound or guessed_letter >= upper_bound or len(guessed_letter) > 1:
            print('Invalid entry')
            guesses += 1
        #low bound < comp letter < guess
        elif computer_letter < guessed_letter:
            upper_bound = guessed_letter
            guesses += 1
        #guess < comp letter < upper bound
        elif guessed_letter < computer_letter:
            lower_bound = guessed_letter
            guesses += 1
        #right answer
        else:
            print('You are correct! The computer selected the letter',computer_letter,'!')
            break
        
    print('You guessed in', guesses, 'tries!!')


def main():
    #main entry point

    #choose an uppercase letter at random:
    computer_letter = random.choice(string.ascii_uppercase[1:-1])

    #start the game!
    guessing_game(computer_letter)


if __name__ == '__main__':
    main()
