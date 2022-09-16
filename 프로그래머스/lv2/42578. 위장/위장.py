def solution(clothes):
    answer = 1
    closet = {}
    
    for name, variety in clothes:
        if variety in closet: # 해시가 있는지 확인할 때. variety[closet] (X) 왜?
            closet[variety] += 1
        else:
            closet[variety] = 1
            
    for key, value in closet.items():
        answer *= (value+1)
        
    answer -= 1 
    return answer