# --------------------------------
#
# Student Name:Lucas Antonsen
# Student Number:
# Assignment 5: Haiku Generator
#
# Date Created:Nov 16/17
# Python Version: 3.6.2
# --------------------------------

import random

haiku_def = {1: 5, 2: 7, 3: 5}

#By Instr. Colin Dyck
def split_line(line):
    '''

    :param line: comma-delimitted line of words/phrases
    :return: list of elements split from a comma
    '''

    phrases = []
    for phrase in line.split(','):
        phrases.append(phrase.strip())

    return phrases


#By Instr. Colin Dyck
def load_season_words(file_path):
    '''
    loads words into a dictionary where key: season value: list of words

    :return: list of words
    '''

    season_words = {}

    with open(file_path, 'r') as words:
        season_words['spring'] = split_line(words.readline())
        season_words['summer'] = split_line(words.readline())
        season_words['autumn'] = split_line(words.readline())
        season_words['winter'] = split_line(words.readline())

    return season_words


#By Instr. Colin Dyck
def load_cmu_words(file_path):
    '''
    loads words into a list

    :return: list of words
    '''

    with open(file_path, 'r') as words:
        word_list = [word.strip() for word in words]

    return word_list


#By Instr. Colin Dyck
def load_syllables(lines):
    '''
    creates a word-syllable count dictionary from incoming list of cmu lines
    :param lines: list of lines from cmu pronounciation dictionary
    :return: word-syllable count dictionary
    '''

    word_syllables = {}

    #loop through all the lines
    for line in lines:
        syllable_count = 0

        #split the line into a list with each element separated by space
        parts = line.split()

        #count the syllables
        for part in parts[1:]:
            #check last character of the part
            if len(part) > 0 and part[-1] in ['0', '1', '2']:
                syllable_count += 1

        #add entry {lower case word: syllable count}
        word_syllables[parts[0].lower()] = syllable_count

    return word_syllables


def count_syllables(phrase, word_syllables):
    '''
    counts syllables in a phrase
    :param phrase: haiku phrase
    :return: number of syllables: 0 represents at least one word not found in the syllable dictionary
    '''
    
    #returns syllable count of the phrase
    count = 0
    for word in phrase.split():
        
        #checks lowercase version of phrase in word_syllables
        if word.lower() not in word_syllables:
            return 0
        else:
            count += word_syllables[word.lower()]

    return count


def generate_line(list_of_phrases, word_syllables, number_of_syllables):
    '''
    generate a single haiku line

    :param list_of_phrases: the list of haiku phrases to choose from
    :param word_syllables: dictionary of word-syllable pairs
    :param number_of_syllables: number of syllables to create for a haiku line
    :return: haiku line with correct amount of syllables
    '''
    
    #line refers to our haiku line as a list
    line = []
    
    #sylcount refers to the total syllables of our line as it is being built
    sylcount = 0
    
    while sylcount != number_of_syllables:
        
        phrase = random.choice(list_of_phrases)
        
        #returns total word count of phrase
        count = count_syllables(phrase, word_syllables)
        
        if 0 < count <= number_of_syllables and sylcount + count <= number_of_syllables:
            
            #adds phrase to our list
            line.append(phrase)
            sylcount += count

    #forms complete line        
    line = ' '.join(line)
    
    return line

    #return 'this should be {0} syllables'.format(number_of_syllables)

            
def generate_haiku(haiku_words, word_syllables):
    '''
    generate a complete haiku
    :param season: season to choose the words from
    :return: None
    '''

    #turns haiku_def into a list of tuples and iterates through the list building a haiku line with syllable count = syllables
    for line, syllables in haiku_def.items():
        print(generate_line(haiku_words, word_syllables, syllables))
        
    #print('build a haiku')


def main():
    '''
    main entry point of program

    :return: None
    '''

    #load word syllable dictionary
    word_list = load_cmu_words('cmu_dictionary.txt')
    word_syllables = load_syllables(word_list)

    #load all haiku words
    haiku_words = load_season_words('haiku_sources.txt')

    #print('some sample words: {0}'.format(','.join(haiku_words['spring'][:5])))
    #print('some sample words: {0}'.format(','.join(haiku_words['summer'][:5])))
    #print('some sample words: {0}'.format(','.join(haiku_words['autumn'][:5])))
    #print('some sample words: {0}'.format(','.join(haiku_words['winter'][:5])))

    #generate one for each season

    print('Spring:')
    generate_haiku(haiku_words['spring'], word_syllables)

    print('\r\nSummer:')
    generate_haiku(haiku_words['summer'], word_syllables)

    print('\r\nAutumn:')
    generate_haiku(haiku_words['autumn'], word_syllables)

    print('\r\nWinter:')
    generate_haiku(haiku_words['winter'], word_syllables)

    #this is useful to count the syllables of a line when in doubt
    #print(count_syllables('long night wild geese pear long night', word_syllables))
  
if __name__ == '__main__':
    main()


