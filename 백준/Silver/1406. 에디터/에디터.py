import sys
from collections import deque
input = sys.stdin.readline

def main():
    left = deque(input().strip())
    right = deque()
    m = int(input())
    # print(left)
    while m:
        cmd = input().split()
        if cmd[0] == 'P':
            left.append(cmd[1])
        elif cmd[0] == "L":
            if left:
                right.appendleft(left.pop())
        elif cmd[0] == "D":
            if right:
                left.append(right.popleft())
        else:
            if left:
                left.pop()
        m -= 1
    print(''.join(left+right))

main()