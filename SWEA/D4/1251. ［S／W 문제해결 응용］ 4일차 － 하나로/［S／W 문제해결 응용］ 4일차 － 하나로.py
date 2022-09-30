def find_set(x):
    if x == p[x]:
        return x
    else:
        return find_set(p[x])


def kruskal():
    cnt = 0
    total = 0
    for i in range(len(arr)):
        p1 = find_set(arr[i][0])
        p2 = find_set(arr[i][1])
        if p1 != p2:
            total += arr[i][2]
            cnt += 1
            p[p2] = p1
        if cnt == N:
            break
    return total


T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    X = list(map(int, input().split()))
    Y = list(map(int, input().split()))
    E = float(input())
    arr = []
    for i in range(N):
        for j in range(i + 1, N):
            arr.append([i, j, E * ((X[i]-X[j])**2+(Y[i]-Y[j])**2)])
    arr.sort(key=lambda x: x[2])
    p = [i for i in range(N + 1)]
    print(f'#{test_case} {round(kruskal())}')