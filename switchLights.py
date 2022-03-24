def solution(a):
    l = []
    for i in a:
        if i == 1: 
            l = [1-i for i in l] + [0]
        else: l += [0]
    return l
