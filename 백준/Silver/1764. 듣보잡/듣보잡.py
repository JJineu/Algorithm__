import sys
input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
deud = set()
bo = set()
for _ in range(n):
    deud.add(input().rstrip())
for _ in range(m):
    bo.add(input().rstrip())

answer = list(deud & bo)
answer.sort()

print(len(answer))
for i in answer:
    print(i)