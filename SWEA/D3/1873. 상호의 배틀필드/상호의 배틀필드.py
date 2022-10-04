T = int(input())
for test_case in range(1, T + 1):
    H, W = map(int, input().split())
    arr = [list(map(str, input())) for i in range(H)]
    N = int(input())
    command = input()
    for i in range(N):
        for j in range(H):
            for k in range(W):
                if arr[j][k] in ['^', 'v', '<', '>']:
                    idx_i, idx_j = j, k
        if command[i] == 'U':
            arr[idx_i][idx_j] = '^'
            if idx_i > 0:
                if arr[idx_i - 1][idx_j] == '.':
                    arr[idx_i][idx_j] = '.'
                    arr[idx_i - 1][idx_j] = '^'
        if command[i] == 'D':
            arr[idx_i][idx_j] = 'v'
            if idx_i < H - 1:
                if arr[idx_i + 1][idx_j] == '.':
                    arr[idx_i][idx_j] = '.'
                    arr[idx_i + 1][idx_j] = 'v'
        if command[i] == 'L':
            arr[idx_i][idx_j] = '<'
            if idx_j > 0:
                if arr[idx_i][idx_j - 1] == '.':
                    arr[idx_i][idx_j] = '.'
                    arr[idx_i][idx_j - 1] = '<'
        if command[i] == 'R':
            arr[idx_i][idx_j] = '>'
            if idx_j < W - 1:
                if arr[idx_i][idx_j + 1] == '.':
                    arr[idx_i][idx_j] = '.'
                    arr[idx_i][idx_j + 1] = '>'
        if command[i] == 'S':
            if arr[idx_i][idx_j] == '<':
                il = 0
                while il <= idx_j:
                    if arr[idx_i][idx_j - il] == '*':
                        arr[idx_i][idx_j - il] = '.'
                        break
                    elif arr[idx_i][idx_j - il] == '#':
                        break
                    il += 1
            if arr[idx_i][idx_j] == '>':
                ir = 0
                while idx_j + ir < W:
                    if arr[idx_i][idx_j + ir] == '*':
                        arr[idx_i][idx_j + ir] = '.'
                        break
                    elif arr[idx_i][idx_j + ir] == '#':
                        break
                    ir += 1
            if arr[idx_i][idx_j] == '^':
                iu = 0
                while iu <= idx_i:
                    if arr[idx_i - iu][idx_j] == '*':
                        arr[idx_i - iu][idx_j] = '.'
                        break
                    elif arr[idx_i - iu][idx_j] == '#':
                        break
                    iu += 1
            if arr[idx_i][idx_j] == 'v':
                id_ = 0
                while id_ + idx_i < H:
                    if arr[idx_i + id_][idx_j] == '*':
                        arr[idx_i + id_][idx_j] = '.'
                        break
                    elif arr[idx_i + id_][idx_j] == '#':
                        break
                    id_ += 1
    print(f'#{test_case}', end=' ')
    for i in range(H):
        print(''.join(arr[i]))
