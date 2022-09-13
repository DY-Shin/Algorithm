def pre_order(n):
    if len(tree[n]) == 2:
        return int(tree[n][1])
    else:
        L = pre_order(int(tree[n][2]))
        R = pre_order(int(tree[n][3]))

        if tree[n][1] == '+':
            return L + R
        elif tree[n][1] == '-':
            return L - R
        elif tree[n][1] == '*':
            return L * R
        elif tree[n][1] == '/':
            return L // R

T = 10
for test_case in range(1, T + 1):
    N = int(input())
    tree = [0 for _ in range(N + 1)]
    for _ in range(N):
        tmp = input().split()
        tree[int(tmp[0])] = tmp

    print(f'#{test_case} {pre_order(1)}')
