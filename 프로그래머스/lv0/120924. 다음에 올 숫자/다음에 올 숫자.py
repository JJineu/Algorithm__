def solution(common):
    answer = 0

    d1 = common[1] - common[0]
    d2 = common[2] - common[1]
    
    if d1 == d2:
        answer = common[-1] + d1
    else:
        if common[-1] == 0:
            answer = 0
        else:
            answer = common[-1] * (d2/d1)
    
    return answer