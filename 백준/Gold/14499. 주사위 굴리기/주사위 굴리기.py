def turn(dire):
    a, b, c, d, e, f = dice[0], dice[1], dice[2], dice[3], dice[4], dice[5]
    if dire == 1:
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = d, b, a, f, e, c
    elif dire == 2:
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = c, b, f, a, e, d
    elif dire == 3:
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = e, a, c, d, f, b
    else:
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = b, f, c, d, a, e


N, M, x, y, K = map(int, input().split())
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
dice = [0, 0, 0, 0, 0, 0]
board = [list(map(int, input().split())) for _ in range(N)]
order = list(map(int, input().split()))

nx, ny = x, y
for i in order:
    nx = nx + dx[i - 1]
    ny = ny + dy[i - 1]
    if nx < 0 or nx >= N or ny < 0 or ny >= M:
        nx = nx - dx[i - 1]
        ny = ny - dy[i - 1]
        continue
    turn(i)
    if board[nx][ny] == 0:
        board[nx][ny] = dice[-1]
    else:
        dice[-1] = board[nx][ny]
        board[nx][ny] = 0
    print(dice[0])
