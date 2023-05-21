import heapq
import sys
input = sys.stdin.readline

N = int(input())
que = []
heapq.heapify(que)
for i in range(N):
    value = int(input())
    if value == 0:
        if que:
            print(heapq.heappop(que))
        else:
            print(0)
    else:
        heapq.heappush(que, value)
