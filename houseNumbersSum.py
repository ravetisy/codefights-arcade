def solution(inputArray):
    sum = 0
    for i in range(len(inputArray)):
        if inputArray[i] == 0:
            return sum    
        sum += inputArray[i]

def solution(inputArray):
    return sum(inputArray[:inputArray.index(0)])
