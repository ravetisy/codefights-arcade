"""Given two strings, write a method to decide if one is a permutation of
the other.

Solution #1: Sort the strings. If two strings are permutations,
then we know they have the same characters, but in different orders.
Therefore, sorting the strings will put the characters from two permutations
in the same order. We just need to compare the sorted versions of the
strings.

Solutions #2: We can also use the definition of a permutation-two words with
the same character counts-to implement this algorithm. We simply iterate
through this code, counting how many times each character appears. Then,
afterwards, we compare the two arrays
"""


def are_permutation(s1: str = '', s2: str = '') -> bool:
    if len(s1) != len(s2):
        return False

    letter_dict = dict()

    for character in s1:
        if character not in letter_dict.keys():
            letter_dict[character] = 1
        letter_dict[character] += 1
    #     print(character)
    #
    # print(letter_dict)

    for character in s2:
        letter_dict[character] -= 1
        if letter_dict[character] < 0:
            return False

    return True


if __name__ == '__main__':
    s1 = 'ashotik'
    s2 = 'kitohsa'

    print(are_permutation(s1=s1, s2=s2))
