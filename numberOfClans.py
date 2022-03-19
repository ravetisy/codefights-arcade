def solution(divisors, k):
    clan = []
    for i in range(1,k+1):
        vec = []
        for j in range(0,len(divisors)):
            if i%divisors[j]==0:
                vec.append(1)
            else:
                vec.append(0)
        clan.append(vec)
    
    clanSet = []
    for i in range(0,len(clan)):
        if clan[i] not in clanSet:
            clanSet.append(clan[i])
    
    return len(clanSet) 
    
    # another solution very simple with set()
    def solution(divisors, k):
    a=set()
    for x in range(1, k+1):
        s=''
        for y in divisors:
            if x%y==0:
                s+='1'
            else:
                s+='0'
        a.add(s)
    return len(a)
    
    #pythonic solution with generator expressions.
    def solution(divisors, k):
        return len(set(tuple(i % d == 0 for d in divisors) for i in range(1, k+1)))
