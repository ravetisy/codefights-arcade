"""Given a string, write a function to check if it is a permutation of a
palindrome. A palindrome is a word or phrase that is the same forwards and
backwards. A permutation is a rearrangement of letters. The palindrome does
not need to be limited to just dictionary words. EXAMPLE

Input: Tact Coa
Output: True (permutations: "taco cat'; "atc o eta·; etc.)

A palindrome is a string that is the same forwards and backwards. Therefore,
to decide if a string is a permutation of a palindrome, we need to know if
it can be written such that it's the same forwards and backwards. What does
it take to be able to write a set of characters the same way forwards and
backwards? We need to have an even number of almost all characters, so that
half can be on one side and half can be on the other side. At most one
character (the middle character) can have an odd count.

"""


def is_palindrome_permutation(string: str = ''):
    if string == '':
        return False
    if len(string) == 1:
        return True

    # the general idea , is that if it's a palindrome permutation, we should
    # check if palindrome string can be formed from the input string. if its
    # can be done, then any input string permutation can be reconstructed in
    # to palindrome string.
    # there is one special case, when the string length is odd, in that
    # case only one character have to be odd(1) and that should be the middle
    # character.
    # we also have to remove the white spaces in the resulted string, because
    # the whitespace can affect the string count, and in result the login
    # written in the code.

    character_count = dict()

    # make characters to lower, because its doesn't matter
    inputString_toList = ''.join(string.split())
    inputString_toList = [char.lower() for char in inputString_toList]
    for character in inputString_toList:
        if character not in character_count.keys():
            character_count[character] = 1
        else:
            character_count[character] += 1

    if len(inputString_toList) % 2 == 0:
        for value in character_count.values():
            if value % 2 != 0:
                return False

    odd_count = 0
    for value in character_count.values():
        if value == 1:
            odd_count += 1

    if odd_count > 1:
        return False

    return True


if __name__ == '__main__':
    input_string = 'Tact Coa'
    print(is_palindrome_permutation(string=input_string))


