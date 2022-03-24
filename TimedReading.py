import re
pattern = '([a-zA-Z]*)'

def solution(maxLength, text):
    match = re.findall(pattern, text)
    count = 0
    print(match)
    if match:
        for word in match:
            if word != '':
                print(word)
                if len(word)<=maxLength:
                    count +=1
    return count

