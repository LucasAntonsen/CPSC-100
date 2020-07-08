#--------------------------------
#
# Student Name:Lucas Antonsen
# Student Number:
# Assignment 1: Right Justify
#
# Date Created:Sept 21/17
# Python Version: 3.6.2
#--------------------------------

import os
import sys


def right_justify(s):
    #The function needs to return(spaces*(70 - (the length of the string)) + the string)
    return (' '*(70-len(s))+ s)


def main():
    print(right_justify('My cat\'s name is Mittens'))


main()
