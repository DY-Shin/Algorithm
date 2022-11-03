from itertools import permutations

def baseball(n):
    global score
    if n == 1:
        score += base[2]
        base[0], base[1], base[2] = 1, base[0], base[1]
    elif n == 2:
        score += base[1] + base[2]
        base[0], base[1], base[2] = 0, 1, base[0]
    elif n == 3:
        score += base[0] + base[1] + base[2]
        base[0], base[1], base[2] = 0, 0, 1
    elif n == 4:
        score += base[0] + base[1] + base[2] + 1
        base[0], base[1], base[2] = 0, 0, 0

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
order = [0] * 9
order[3] = 0
player = [i for i in range(1, 9)]
nPr = list(permutations(player, 8))
max_score = 0
for i in range(len(nPr)):
    order[0], order[1], order[2], order[4], order[5], order[6], order[7], order[8] = nPr[i]
    score = 0
    inning = 0
    out = 0
    base = [0] * 3
    while inning < N:
        for j in range(9):
            if arr[inning][order[j]] == 0:
                out += 1
            else:
                baseball(arr[inning][order[j]])

            if out >= 3:
                inning += 1
                base = [0] * 3
                out = 0

            if inning >= N:
                break

    if score >= max_score:
        max_score = score
print(max_score)