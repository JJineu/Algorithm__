import sys
input = sys.stdin.readline

n, m = map(int, input().split())
poket_key = {}
poket_value = {}
for i in range(n):
    name = input().strip()
    poket_key[i] = name
    poket_value[name] = i
    
for _ in range(m):
    cmd = input().strip()
    if cmd.isdigit():
        print(poket_key[int(cmd)-1])
    if cmd.isalpha():
        print(poket_value[cmd]+1)
