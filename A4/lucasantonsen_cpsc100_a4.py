#--------------------------------
#
# Student Name:Lucas Antonsen
# Student Number:
# Assignment 4: Rock Paper Scissors Spock Lizard
#
# Date Created:Nov 1/17
# Python Version: 3.6.2
#--------------------------------

import os
import sys
import random
random.seed(3245234324)

#list of possible moves in rock, paper, scissors, spock, lizard
valid_moves = ['Rock', 'Paper', 'Scissors','Spock','Lizard']

#dictionary of defined rules for the game
rules = {
    'Rock': {'beats': ['Scissors', 'Lizard'], 'verb': ['smashes', 'crushes']},
    'Paper': {'beats': ['Rock', 'Spock'], 'verb': ['smothers', 'disproves']},
    'Scissors': {'beats': ['Paper', 'Lizard'], 'verb': ['cuts', 'decapitates']},
    'Spock': {'beats': ['Scissors', 'Rock'], 'verb': ['smashes', 'vaporizes']},
    'Lizard': {'beats': ['Spock', 'Paper'], 'verb': ['poisons', 'eats']}
}


def get_player_throw():
    '''
    player throw, typed in from stdin
    :return: user input
    '''
    return random.choice(valid_moves)


def get_outcome(player_one_throw, player_two_throw):
    '''
    :param player_throw: result of player throw
    :param computer_throw: result of computer throw
    :return: string of outcome
    '''
    #we will have two items in our dictionary referring to the two parts of the assignment
    outcome = {}

    #get the dictionaries based on the player throws
    player_one_rules = rules[player_one_throw]
    player_two_rules = rules[player_two_throw]

    #determine outcome
    if player_one_throw == player_two_throw:
        outcome[0] = 'Tie! Both players pick {0}!!'.format(player_one_throw)
        outcome[1] = 'Tie'

    #if player_two_throw is in the list of the items that player_one_throw beats
    elif player_two_throw in player_one_rules['beats']:
        
        #defines the verb corresponding to the throw that player_one_throw beats
        if player_two_throw == player_one_rules['beats'][0]:
            idx = 0
        else:
            idx = 1
            
        outcome[0] = 'Player 1 wins! {0} {1} {2}!!'.format(player_one_throw, player_one_rules['verb'][idx], player_two_throw)
        #player_one_throw wins under this condition therefore
        outcome[1] = player_one_throw
        
    #if player_one_throw is in the list of the items that player_two_throw beats
    elif player_one_throw in player_two_rules['beats']:
        
        #defines the verb corresponding to the throw that player_two_throw beats
        if player_one_throw == player_two_rules['beats'][0]:
            idx = 0
        else:
            idx = 1
        outcome[0] = 'Player 2 wins! {0} {1} {2}!!'.format(player_two_throw, player_two_rules['verb'][idx], player_one_throw)
        #player_two_throw wins under this condition therefore
        outcome[1] = player_two_throw
        
    else:
        #we shouldn't ever get here
        outcome = 'Invalid!!'

    return outcome


def main():
    '''
    main part of program
    :return:
    '''
    
    #part 1
    print('Part 1\r\n')
    count = 10
    for i in range(count):
        
        # get throws
        player_one_throw = get_player_throw()
        player_two_throw = get_player_throw()
        
        #result = the [0] key of the outcome dictionary
        result = get_outcome(player_one_throw, player_two_throw)[0]
        print('Game {0}: {1}'.format(i + 1, result))

    #part 2
    print('\r\nPart 2\r\n')
    
    #collection results of winning weapon
    results = {}
    count = 100000
    for i in range(count):
        
        # get throws
        player_one_throw = get_player_throw()
        player_two_throw = get_player_throw()
        
        #result = the [1] key of the outcome dictionary
        result = get_outcome(player_one_throw, player_two_throw)[1]
        
        #adds the winners as keys to the dictionary and their corresponding value refers to how many times the key has won
        results[result] = results.get(result, 0) + 1
        

        #you need to fill the dictionary with the winning weapon

    print(results)

if __name__ == '__main__':
    main()
