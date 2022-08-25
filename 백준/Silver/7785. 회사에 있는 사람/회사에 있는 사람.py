from sys import stdin
input = stdin.readline

n = int(input())
h = {}
for i in range(n):
    name, log = map(str, input().split())
    if log == "enter":
        h[name] = 1
    else:
        if h[name]:
            del h[name]

for i in sorted(h, reverse=True):
    print(i) 