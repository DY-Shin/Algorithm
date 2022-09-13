def subset(idx, ssum):
    global cnt

    if idx >= N:
        return

    ssum += arr[idx]

    if ssum == S:
        cnt += 1

    # 현재 arr[idx]를 선택한 경우의 가지
    subset(idx + 1, ssum)

    # 현재 arr[idx]를 선택하지 않은 경우의 가지
    subset(idx + 1, ssum - arr[idx])


N, S = map(int, input().split())
arr = list(map(int, input().split()))
cnt = 0

subset(0, 0)
print(cnt)