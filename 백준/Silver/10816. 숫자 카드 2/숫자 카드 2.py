import sys
input = sys.stdin.readline
from collections import Counter


n = int(input())
card = list(map(int, input().strip().split()))
m = int(input())
get_card = list(map(int, input().strip().split()))

s = Counter(card)
# print(s)
answer = []
for i in get_card:
    if s[i] :
        answer.append(s[i])
    else:
        answer.append(0)
print(" ".join(list(map(str, answer))))