# def solution(s):
#     answer = 0
#     # 앞 뒤 포인터써서 같은 문자인지 확인
#     # 중간에 달라지면 다시
#     # 같은 인덱스까지 왔을때 (홀수) -> return
#     # 뒤 포인터부터 전부탐색
#     # 앞 포인터 한칸씩 전진
#     front, back = 0, n-1
#     n = len(s)
    
#     for i in range(n):
#         tmp = n-i
#         if s[i] == s[tmp]:
#             while front > back:
#                 if s[front] == s[back]:
#                     front += 1
#                     back += -1
#                 else:
#                     break
#         else:
                    
#     return answer


# def solution(s):
#     answer = 1
#     l = len(s)
 
#     for start in range(l):
#         for end in range(start + 2, l + 1):
#             a = s[start:end]
#             if len(a) < answer:
#                 continue
#             if a == a[::-1]:
#                 answer = max(answer, end - start)
#     return answer

def solution(s):
    lbound=0
    rbound=0
    maxlength=0

    while lbound<len(s) and rbound<len(s):
        lb = lbound
        rb = rbound
        while lb>=0 and rb<len(s):
            if s[lb]==s[rb]:
                maxlength = max(maxlength, rb-lb+1)
                # print("lb = %d, rb = %d" % (lb, rb))
                lb -=1
                rb +=1
            else:
                break
        if lbound == rbound:
            rbound += 1
        else:
            lbound += 1
    return maxlength