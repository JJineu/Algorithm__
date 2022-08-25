n, m = map(int, input().split())
deud = set()
bo = set()
for _ in range(n):
    deud.add(input())
for _ in range(m):
    bo.add(input())

answer = sorted(list(deud & bo))

print(len(answer))
for i in answer:
    print(i)