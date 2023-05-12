import sys
input = sys.stdin.readline

N, M = map(int, input().strip().split())
keyword = set()
answer = []
for _ in range(N):
    word = input().strip()
    keyword.add(word)
for _ in range(M):
    post = input().strip().split(",")
    for i in range(len(post)):
        keyword.discard(post[i])
    print(len(keyword))
