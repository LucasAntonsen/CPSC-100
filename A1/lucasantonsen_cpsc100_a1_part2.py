#--------------------------------
#
# Student Name:Lucas Antonsen
# Student Number:
# Assignment 1: Rock Paper Scissors
#
# Date Created:Sept 21/17
# Python Version: 3.6.2
#--------------------------------

import os
import sys
import random
#random.seed(100)

#list of possible moves in rock, paper, scissors
valid_moves = ['Rock','Paper','Scissors']


def get_computer_throw():
    #Computer chooses a random throw
    return random.choice(valid_moves)


def get_player_throw():
    #Player chooses a throw
    throw = input('Enter Rock, Paper, Scissors (or x to exit): ')
    return throw


def get_outcome(player_throw, computer_throw):
    #Draw
    if player_throw == computer_throw:
        result = 'Draw!'
    #Paper beats Rock
    elif player_throw == 'Paper' and computer_throw == 'Rock':
        result = 'Paper beats Rock, Player wins!'
    #Paper loses to Scissors
    elif player_throw == 'Paper' and computer_throw == 'Scissors':
        result = 'Scissors beats Paper, Computer wins!'
    #Scissors loses to Rock
    elif player_throw == 'Scissors' and computer_throw == 'Rock':
        result = 'Rock beats Scissors, Computer wins!'
    #Scissors beats Paper
    elif player_throw == 'Scissors' and computer_throw == 'Paper':
        result = 'Scissors beats Paper, Player wins!'
    #Rock beats Scissors
    elif player_throw == 'Rock' and computer_throw == 'Scissors':
        result = 'Rock beats Scissors, Player wins!'
    #Rock loses to Paper
    elif player_throw == 'Rock' and computer_throw == 'Paper':
        result = 'Paper beats Rock, Computer wins!'
    #Invalid throw
    else:
        result = 'Invalid throw from player. Please choose Rock, Paper, or Scissors.'
    return result

def main():

    while True:
        # get throws
        player_throw = get_player_throw()
        computer_throw = get_computer_throw()

        if player_throw == 'x':
            break

        print('Player picks: ' + player_throw)
        print('Computer picks: ' + computer_throw)

        #Call get_outcome and return result
        print(get_outcome(player_throw, computer_throw))

    print('Thanks for playing!')

if __name__ == '__main__':
    main()
