from collections import deque


def zero_group_check(start_r, start_c):
    queue = deque([[start_r, start_c]])
    visited[start_r][start_c] = group_num
    group_cnt_dict[group_num] = 1
    while queue:
        r, c = queue.popleft()

        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if nr < 0 or nr >= N or nc < 0 or nc >= M or visited[nr][nc] != 0 or arr[nr][nc] == 1:
                continue
            visited[nr][nc] = group_num 
            group_cnt_dict[group_num] += 1
            queue.append([nr, nc])


def cnt_check(start_r, start_c):
    for i in range(4):
        nr = start_r + dr[i]
        nc = start_c + dc[i]

        if nr < 0 or nr >= N or nc < 0 or nc >= M or arr[nr][nc] == 1 or not visited[nr][nc]:
            continue
        if not group_check.get(visited[nr][nc], 0):
            arr[start_r][start_c] += group_cnt_dict.get(visited[nr][nc], 0)
            arr[start_r][start_c] %= 10 
            group_check[visited[nr][nc]] = 1


N, M = map(int, input().split())
arr = [list(map(int, input())) for _ in range(N)]
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]
group_num = 1
group_cnt_dict = {}

visited = [[0] * M for _ in range(N)]
for i in range(N):
    for j in range(M):
        if arr[i][j] == 0 and visited[i][j] == 0:
            zero_group_check(i, j)
            group_num += 1  
            
for i in range(N):
    for j in range(M):
        if arr[i][j] == 1:
            group_check = {}
            cnt_check(i, j)

for i in range(N):
    for j in range(M):
        print(arr[i][j], end="")
    print()