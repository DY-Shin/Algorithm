N = int(input())
graph = [input() for _ in range(N)]
body = []
left_arm = 0
right_arm = 0
waist = -1
left_leg = 0
right_leg = 0
for i in range(N):
    for j in range(N):
        if graph[i][j] == '*':
            body.append([i, j])
print(body[0][0] + 2, body[0][1] + 1)
for i in range(len(body)):
    if body[i][0] == body[0][0] + 1:
        if body[i][1] < body[0][1]:
            left_arm += 1
        elif body[i][1] > body[0][1]:
            right_arm += 1
    elif body[i][1] == body[0][1]:
        waist += 1
    elif body[i][1] == body[0][1] - 1:
        left_leg += 1
    elif body[i][1] == body[0][1] + 1:
        right_leg += 1
print(left_arm, right_arm, waist, left_leg, right_leg)
