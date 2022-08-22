T = 10
for test_case in range(1, T + 1):  # 1 : 빨간색  2 : 파란색
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    cnt = 0

    for i in range(N):
        for j in range(N):
            stack = []
            if arr[j][i] == 1:
                stack.append('1')
                for k in range(j + 1, N):
                    if arr[k][i] == 1:
                        stack.append('1')
                    elif arr[k][i] == 2:
                        stack.pop()
                        stack.append('3')
                if '3' not in stack:
                    stack = []
                if stack:
                    for l in range(len(stack)):
                        if stack[l] == '3':
                            cnt += 1
            else:
                continue
            break

    print(f'#{test_case} {cnt}')