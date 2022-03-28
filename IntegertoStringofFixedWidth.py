# Given a positive integer number and a certain length, we need to modify the given number to have a specified length. We are allowed to do that either by cutting out leading digits (if the number needs to be shortened) or by adding 0s in front of the original number.

# Example

#     For number = 1234 and width = 2, the output should be
#     solution(number, width) = "34";
#     For number = 1234 and width = 4, the output should be
#     solution(number, width) = "1234";
#     For number = 1234 and width = 5, the output should be
#     solution(number, width) = "01234".


def solution(number, width):
    new_number = ''
    if len(str(number)) == width:
        return new_number + str(number)
    if len(str(number)) < width:
        new_number += (width - len(str(number)))*'0' + str(number)
        return new_number
    else:
        new_number += str(number)[len(str(number))-width:]
        return new_number
