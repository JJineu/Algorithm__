def solution(M, N):
    answer = 0
    if M == 1 and N == 1:
        return 0
    answer = M * (N-1) + M-1
    return answer