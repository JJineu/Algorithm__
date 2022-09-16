def solution(s):
    answer = []
    
    tmp = s
    zero = 0
    all_cnt = 0
    while len(tmp) > 1:
        cnt = 0
        for i in range(len(tmp)):
            if tmp[i] == "1":
                cnt += 1
            else:
                zero += 1
                # print(tmp[i])
        # print(cnt)
        tmptmp = []
        while cnt // 2:
            tmptmp.append(cnt%2)
            cnt //= 2 
        tmptmp.append(cnt)
        tmptmp.reverse()
        tmp = tmptmp
        # print(tmp)
        tmp = ''.join(list(map(str, tmp)))
        # print(tmp)
        all_cnt +=1
         
    return [all_cnt, zero]