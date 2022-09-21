def multi(num):
    global cnt
    if num > 9:
        num = str(num)
        ssum = 0
        for i in num:
            ssum += int(i)
        cnt += 1
        multi(ssum)
    else:
        print(cnt)
        if num % 3:
            print('NO')
        else:
            print('YES')


N = int(input())
cnt = 0
multi(N)
