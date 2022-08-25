from sys import stdin
input = stdin.readline

n = int(input())
h = {}
for i in range(n):
    name, log = map(str, input().split())
    if log == "enter":
        h[name] = 1
    else:
        del h[name]
sorted_h = sorted(h.keys(), reverse=True)
# print(sorted_h)
for i in range(len(sorted_h)):
    print(sorted_h[i])    