def solution(num, total):
    answer = []
    if num%2:
        start = total//num - num//2
        for n in range(start, start+num):
            answer.append(n)
    else:
        start = total//num - num//2 + 1
        for n in range(start, start+num):
            answer.append(n)
        
    return answer