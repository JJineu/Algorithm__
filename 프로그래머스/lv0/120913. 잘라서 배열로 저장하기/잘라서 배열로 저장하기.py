# def solution(my_str, n):
#     answer = []

#     tmp = 0
#     for i in range(n,len(my_str)+1,n):
#         tmp = i
#         answer.append(my_str[i-n:i])
#     if len(my_str)%n:
#         answer.append(my_str[tmp:])
#     # print(tmp)
#     return answer

# 1
# 2
# 3
# 4
# 5
# 6
def solution(my_str, n):
    answer = []
    for i in range(0, len(my_str), n):
        answer.append(my_str[i:i+n])
    return answer