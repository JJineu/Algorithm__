def solution(n):
    answer = 0
    d = [0]*(n+1)
    
    if n == 1:
        return 1
    if n == 2 :
        return 2
    
    d[1] = 1
    d[2] = 1
    
    for i in range(2,n+1):
        d[i] = d[i-1]+d[i-2]
        d[i] %= 1234567
    
    return d[n] %1234567