def solution(clothes):
    answer = 1
    closet = {}
    
    for name, variety in clothes:
        if variety in closet:
            closet[variety] += 1
        else:
            closet[variety] = 1
            
    for key, value in closet.items():
        answer *= (value+1)
        
    answer -= 1 
    return answer