def solution(n):
    answer = 0
    # num = list(x for x in range(2, n+1))
    # print(num)
    prime = [False, False] + [True]*(n-1)
    for i in range(int(n**0.5)+1):
        if prime[i]:
            for j in range(2*i, n+1, i):
                prime[j] = False
    # print(prime)
    for p in prime:
        if p:
            answer += 1            
    return answer