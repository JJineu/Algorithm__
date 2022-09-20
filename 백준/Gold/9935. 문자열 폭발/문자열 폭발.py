from sys import stdin
input = stdin.readline

word = input().strip()
bomb = input().strip()

stack = []

for i in word:
    if i != bomb[-1]:
        stack.append(i)

    else:
        stack.append(i)
        b = len(bomb)
        if ''.join(stack[-b:]) == bomb:
            for _ in range(b):
                stack.pop()

if len(stack) == 0:
    print('FRULA')

else:
    print(''.join(stack))