import sys
input = sys.stdin.readline

n, m = map(int, input().split())
s = set()
for i in range(n):
    s.add(input().rstrip())
    
cnt = 0
for i in range(m):
    check = input().rstrip()
    if check in s:
        cnt += 1
print(cnt)