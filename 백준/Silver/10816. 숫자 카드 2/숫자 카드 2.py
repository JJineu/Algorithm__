import sys
input = sys.stdin.readline
from collections import Counter

n = input()
card = input().strip().split()
m = input()
get_card = input().strip().split()

# print(card)
s = Counter(card)
# print(s)
answer = []
for i in get_card:
    if s[i] :
        answer.append(s[i])
    else:
        answer.append(0)
print(" ".join(list(map(str, answer))))

        