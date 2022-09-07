def solution(distance, rocks, n):
    answer = 0
    
# 바위를 n개 제거함
# itertools combinations -> 시간초과날것

# rocks 정렬 후, 각 바위의 거리 찾아야 함
# rocks + 0, distance
    rocks.append(distance)
    rocks.sort()
# 바위 제거할 때, 거리 중 작은것부터 빼는건?
# 최솟값두고, 그보다 작으면 바위를 뺌

# 바위사이의 거리를 기준으로 제거되는 바위를 셈
    start = 0
    end = distance
    while start <= end:
        mid = (start+end)//2 
        del_rock = 0
        std_rock = 0
        
        for rock in rocks: 
            if del_rock > n:
                break
            if rock - std_rock < mid:
                del_rock += 1
            else:
                std_rock = rock
        
        if del_rock > n:
            end = mid -1
        else:
            start = mid + 1
            answer = mid
    
    return answer