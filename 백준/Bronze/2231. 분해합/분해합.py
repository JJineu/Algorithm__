import sys
input = sys.stdin.readline

def main():
    n = input()
    l = len(n)
    n = int(n)

    start = n - 9*l
    if start < 0:
        start = 0
        
    start = 0
    for num in range(start, n+1):
        sum_num = num
        num = str(num)
        for i in num:
            sum_num += int(i)
        if sum_num == n:
            print(num)
            return
    
    print(0)


main()