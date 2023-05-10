N, score, P = map(int, input().split())
if N == 0:
    print(1)
else:
    rank = list(map(int, input().split()))
    if N == P and rank[-1] >= score:
        print(-1)
    else:
        rank.append(score)
        rank.sort(reverse=True)
        print(rank.index(score) + 1)
