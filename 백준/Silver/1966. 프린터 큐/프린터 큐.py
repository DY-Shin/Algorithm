from collections import deque

T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    Q = deque(arr)
    new_arr = []
    K = [0] * N
    K[M] = 'k'
    K_Q = deque(K)
    new_K = []

    while Q:
        flag = 1
        i = 1
        while i < len(Q):
            if Q[0] < Q[i]:
                flag = 0
                break
            i += 1

        if flag == 0:
            tmp = Q.popleft()
            Q.append(tmp)
            tmp_k = K_Q.popleft()
            K_Q.append(tmp_k)
        else:
            tmp = Q.popleft()
            new_arr.append(tmp)
            tmp_k = K_Q.popleft()
            new_K.append(tmp_k)

    for i in range(N):
        if new_K[i] == 'k':
            idx = i

    print(idx + 1)
