def odd(num):
    if num % 2:
        return (num + 1) // 2
    else:
        return num // 2

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    room = [0] * 201
    result = 0

    for i in range(N):
        n1 = arr[i][0]
        n2 = arr[i][1]
        r1 = odd(n1)
        r2 = odd(n2)
        if r2 > r1:
            for j in range(r1, r2 + 1):
                room[j] += 1
        else:
            for j in range(r2, r1 + 1):
                room[j] += 1

    for i in room:
        if i > result:
            result = i

    print(f'#{test_case} {result}')