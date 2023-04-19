import sys
input = sys.stdin.readline


def dfs(cnt, word):
    if len(word) == k:
        answer.append(word)
        return

    if cnt >= k:
        return

    for i in range(10):
        if not visited[i]:
            if len(word) < 1:
                visited[i] = 1
                dfs(cnt + 1, word + str(i))
                visited[i] = 0
            else:
                if arr[cnt - 1] == ">":
                    if int(word[-1]) > i:
                        visited[i] = 1
                        dfs(cnt + 1, word + str(i))
                        visited[i] = 0
                else:
                    if int(word[-1]) < i:
                        visited[i] = 1
                        dfs(cnt + 1, word + str(i))
                        visited[i] = 0


k = int(input()) + 1
arr = list(input().split())
answer = []
visited = [0] * 10
dfs(0, "")
print(answer[-1])
print(answer[0])

