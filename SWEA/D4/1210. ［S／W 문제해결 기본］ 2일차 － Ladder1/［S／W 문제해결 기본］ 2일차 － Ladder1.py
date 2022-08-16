def find_start(a):
    for i in range(N):
        if arr[N - 1][i] == 2:
            x = N - 1
            y = i
            return x, y

def check(a, x, y):
    if x < 0 or x >= N:
        return False
    if y < 0 or y >= N:
        return False
    if a[x][y] == 0:
        return False
    if a[x][y] == 9:
        return False
    return True

def ladder(a, x, y):
    while True:
        if x == 0:
            return y
        for i in range(3):
            nx = x + dx[i]
            ny = y + dy[i]
            if check(arr, nx, ny):
                x = nx
                y = ny
                a[x][y] = 9  # 방문표시

# 좌우를 먼저 해야함
dx = [0, 0, -1]
dy = [-1, 1, 0]

for test_case in range(1, 11):
    case = int(input())
    N = 100
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 시작점 찾기
    x, y = find_start(arr)

    print(f'#{case} {ladder(arr, x, y)}')