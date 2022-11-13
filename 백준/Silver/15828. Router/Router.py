from collections import deque

N = int(input())
buffer = deque()
while True:
    pack = int(input())
    if pack == -1:
        break
    elif pack == 0:
        buffer.popleft()
    else:
        if len(buffer) < N:
            buffer.append(pack)

if buffer:
    print(*buffer)
else:
    print('empty')
