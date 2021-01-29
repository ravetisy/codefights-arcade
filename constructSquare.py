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
############################## new optimized version ##################
# its more optimized is we start to look for numbers already in square root range of possible soolutions, and if found, rise them to square.
# and one more thing thats makes more easier the solution. In my first solution I considered the all permutations  of current string, that can make the number.
# but this is not needed as we can assign any number to any letter, so the permutation doesnt matter any more. The only thing that matters, are the exact maaping 
# and probable corresposndence of string to leteer. This means that we have to check weahter there are the same amount of chars<=>numbers in both string and number.
# for examble 55687 = aabce, There is no need to check aabce aacbe aaebc versions, The have to only check that there is dsitinct 3 chars in letter and 3 distinct
# numbers in number.
# So goes the solution.

def constructSquare(s):
    for x in range(int(math.sqrt(10**len(s))),0,-1):
        if count(s)==count(str(x**2)):
            return (x**2)
    return -1
    
def count(x):
    l=[]
    for i in set(x):
        l.append(x.count(i))
    return(sorted(l))
