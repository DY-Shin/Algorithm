from itertools import combinations
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
house = [list(map(int, input().split())) for _ in range(N)]
entire = list(range(N))
com = list(combinations(entire, K))
answer = 987654321
for i in range(len(com)):
    shelter = []
    normal = []
    for j in range(N):
        if j in com[i]:
            shelter.append(house[j])
        else:
            normal.append(house[j])

    dis_list = [987654321] * (N - K)
    for j in range(K):
        for k in range(N - K):
            dis = abs(shelter[j][0] - normal[k][0]) + abs(shelter[j][1] - normal[k][1])
            if dis_list[k] > dis:
                dis_list[k] = dis
        if max(dis_list) < answer:
            answer = max(dis_list)

print(answer)
