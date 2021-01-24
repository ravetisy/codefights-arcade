from itertools import permutations
from collections import Counter

def constructSquare(string):
    
    words = []
    for word in permutations(string):
        words.append(''.join(word))
    
    top_bound = math.pow(10, len(string))
    lower_bound = math.pow(10, len(string)-1)
    
    for number in range(int(top_bound), int(lower_bound), -1):
        if number % 10 not in {0, 1, 4, 5, 6, 9}:
            continue
        if isSqare(number):
            for word in words:
                if numberCorrespondsToString(word, number):
                    return number
    return -1

def numberCorrespondsToString(string: str, number: int):
    '''int the context of this chellenge, we assume that
    both length of string and lenght of integer are the same, this are given by the constraints
    and are checked in the main function with the top_bound and lower_bound variables
    '''
    number_map = dict()
    for i in range(len(string)):
        number_map[string[i]] = str(number)[i]
    
    str_number = ''
    for character in string:
        str_number += number_map[character]
    
    return True if int(str_number) == number else False
    
def isSqare(number):
    root = math.sqrt(number)
    if int(root + 0.5) ** 2 == number:
        return True
    else:
        return False
