import sys
input = sys.stdin.readline

def main():
    n = input()
    l = len(n)
    n = int(n)
    
    for num in range(n+1):
        sum_num = num
        num = str(num)
        for i in num:
            sum_num += int(i)
        if sum_num == n:
            print(num)
            return
    
    print(0)


main()