import sys
input = sys.stdin.readline


def bs(title, cnt):
    s, e = 0, len(title) - 1
    res = 0
    while s <= e:
        m = (s + e) // 2
        if int(title[m][1]) >= cnt:
            e = m - 1
            res = m
        else:
            s = m + 1
    return res


N, M = map(int, input().split())
title = [input().split() for _ in range(N)]
for i in range(M):
    cnt = int(input())
    print(title[bs(title, cnt)][0])
