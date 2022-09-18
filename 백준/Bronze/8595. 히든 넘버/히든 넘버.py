def main():
    n = int(input())
    s = list(input())
    d = '0123456789'
    hiddenNum = ""

    for i in s:
        if i in d:
            hiddenNum += i

        else:
            hiddenNum += " "

    print(sum(list(map(int, hiddenNum.split()))))

main()