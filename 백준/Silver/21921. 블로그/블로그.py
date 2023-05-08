import sys
input = sys.stdin.readline

N, X = map(int, input().split())
arr = list(map(int, input().split()))

visit = 0
result = 0

if max(arr) == 0:
    print("SAD")
else:
    for i in range(X):
        visit += arr[i]
    tmp_visit = visit
    result = 1
    for i in range(X, N):
        tmp_visit += arr[i] - arr[i - X]
        if tmp_visit > visit:
            visit = tmp_visit
            result = 1
        elif tmp_visit == visit:
            result += 1
    print(visit)
    print(result)
