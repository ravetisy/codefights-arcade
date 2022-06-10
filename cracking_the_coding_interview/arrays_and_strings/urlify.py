"""Write a method to replace all spaces in a string with '%20'. You may
assume that the string has sufficient space at the end to hold the
additional characters, and that you are given the "true" length of the
string.

EXAMPLE
Input: 'Mr John Smith is in the middle of the situation.'
Output: 'Mr%20John%20Smith'

as our solution is in python, we don't need to calculate the actual real final
length of the string, so the second input argument we don't need.
"""


def urlify(string: str = '') -> str:
    if len(string) == 0:
        return string

    # we will make list form string, then will join them
    list_string = list(string)
    # we will traverse the string and replace all the occurrences of spaces
    # with the characters with inserting characters % 2 and 0 at that place.
    for index in range(len(list_string)-1, -1, -1):
        if list_string[index] == ' ':
            list_string.pop(index)
            list_string.insert(index, '0')
            list_string.insert(index, '2')
            list_string.insert(index, '%')
    return ''.join(list_string)


if __name__ == '__main__':
    string_to_replace = 'Mr John Smith is in the middle of the situation. so '
    final_string = urlify(string=string_to_replace)
    print(final_string)
