def move(arr):
    temp = arr[0]
    arr.pop(0)
    arr.append(temp)
    return arr

T = 10
for test_case in range(1, T + 1):
    case = int(input())
    arr = list(map(int, input().split()))
    flag = 1

    while flag:
        for i in range(1, 6):
            arr[0] = arr[0] - i
            if arr[0] <= 0:
                arr[0] = 0
                move(arr)
                flag = 0
                break
            else:
                move(arr)

    print(f'#{case}', end=' ')
    print(*arr)