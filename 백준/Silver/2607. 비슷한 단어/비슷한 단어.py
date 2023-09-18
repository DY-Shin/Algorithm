N = int(input())
word = list(input())
result = 0
for i in range(N - 1):
    compare = word[:]
    voca = list(input())
    cnt = 0
    for w in voca:
        if w in compare:
            compare.remove(w)
        else:
            cnt += 1

    if cnt < 2 and len(compare) < 2:
        result += 1

print(result)
