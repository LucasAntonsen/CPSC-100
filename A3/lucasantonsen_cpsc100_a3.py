#--------------------------------
#
# Student Name:Lucas Antonsen
# Student Number:
# Assignment 3: Mystery Word
#
# Date Created:Oct 18/17
# Python Version: 3.6.2
#--------------------------------

import random


def load_words(file_path):
    '''
    loads words into a list

    :return: list of words
    '''

    with open(file_path, 'r') as words:
        word_list = [word.strip() for word in words]

    return word_list


def get_hidden_word(word, guessed_letters):
    '''
    generates the hidden version of the word

    eg get_hidden_phrase('POSSIBLE', 'PSB') would return 'P-SS-B--'

    :param word: correct word
    :param guessed_letters: string of letters that the user has guessed so far
    :return: hidden word
    '''
    
    #assigns the variable hidden_word into a list of dashes the same length as the word we are trying to guess
    hidden_word = ['-'] * len(word)
    
    #converts the unknown word into a list for iteration
    list_word = list(word)
    
    #iterates through the list_word and if any letters in that list are in the guessed_letters list the function changes the value of hidden_word to the value of
    #list_word at that index. ie. if our word is AWKWARD and we guess the letter 'A' then the function will iterate over the list version of awkward: [A,W,K,..]
    #and when it comes across an 'A' it will take that value of i and the index and replace the value of that same index on hidden_word with i, which would be:
    #before: ------- after: A---A--
    for i in list_word:
        if i in guessed_letters:
            t = list_word.index(i)
            hidden_word[t] = i
            
            #this enables the function to add multiple copies of a single letter to different indexes in hidden_word rather than just the first instance of that letter.
            list_word[t] = '8'
         
    return hidden_word


#this functions checks to see if the input is valid and returns the original guess or a new guess
def valid_type(guess, guessed_letters):
    
    while True:
        #checks if the guess is one character long
        if len(guess) > 1: 
            guess = input('Sorry, only one letter at a time. Guess a letter: ').upper()
            
        #checks if the guess is a letter   
        elif not guess.isalpha():
            guess = input('Sorry, only letters are accepted. Guess a letter:').upper()
            
        #checks if the guess has already been input
        elif guess in guessed_letters:
            guess = input('You have already guessed the letter {0}. Guess a letter:'.format(guess)).upper()

        #returns the guess if it is valid
        else:
            return guess


def mystery_word(word, allowed_guesses):
    '''
    main logic for game

    :param word: word for the user to guess
    :param allowed_guesses: number of allowed guesses until hanging
    :return: None
    '''
    
    word = word.upper()
    #i set missed_letters and guessed_letters to empty lists so i can append them
    missed_letters = []
    guessed_letters = []
    guesses = allowed_guesses
    guessed_word = ['-']*len(word)

    while guesses > 0 and ''.join(guessed_word) != word:
        
        #.join is used extensively to add the various lists into a string which can be printed
        print('\r\nWord: {0}'.format(''.join(guessed_word)))
        print('Misses:{0} ({1} left)'.format(''.join(missed_letters), guesses))
        
        question = ('Guess a letter:')
        guess = input(question).upper()
        
        #checks if guess is valid and returns a valid guess back to the function
        guess = valid_type(guess, guessed_letters)
        
        if guess not in word:
            #adding items to our missed_letters and guessed_letters lists
            missed_letters.append(guess)
            guessed_letters.append(guess)
            
            #the length of missed letters will determine how many guesses we have left
            guesses = allowed_guesses - len(missed_letters)
            
        else:
            guessed_letters.append(guess)
            
            #calls get_hidden_word function which then changes the value of guessed_word to hidden_word (---A--- , etc) which has our guessed letter in it
            guessed_word = get_hidden_word(word, guessed_letters)
            
            
    #you could loop until player guesses word, or no more guesses
    if ''.join(guessed_word) == word:
        print('\r\nYou solved the puzzle \'{0}\' with {1} missed guesses!'.format(word, len(missed_letters)))
    else:
        print('\r\nToo bad!  The phrase was \'{0}\''.format(word))

    #play again    
    print('\r\nWould you like to play again?')
    main()
        

def main():
    '''
    entry point for file: load words, ask input, play game

    :return: None
    '''

    words = load_words('hangman_words.txt')
    print('There are {0} words'.format(len(words)))

    #these need to be loaded up
    #level_1_2_words = []
    #level_3_words = ??
    level_1_2_words = words[49:]
    level_3_words = words[:49]

    action = input("Enter difficulty level you would like to play at (1-3): ")
    
    while action < '1' or action > '3' or len(action) > 1:
        print("I do not understand. I suggest practicing your keyboard technique!")
        action = input("Enter difficulty level you would like to play at (1-3): ")
    
    #takes value of input and defines word difficulty and allowed_guesses
    if action == '1':
        word = random.choice(level_1_2_words)
        allowed_guesses = 7
        
    elif action == '2':
        word = random.choice(level_1_2_words)
        allowed_guesses = 6
        
    else:
        word = random.choice(level_3_words)
        allowed_guesses = 5
            
    #play the game based on difficulty level
    #below is just a test run
    #mystery_word(words[0], 26)
    mystery_word(word, allowed_guesses)
    

if __name__ == '__main__':
    main()

