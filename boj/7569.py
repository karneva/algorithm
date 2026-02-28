# 백준 7569번: 토마토

import sys
from collections import deque

M, N, H = map(int, input().split())

box = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]

delta = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, 0, 1), (0, -1, 0), (0, 0, -1)]

tomato = deque([])

for z in range(H):
    for x in range(N):
        for y in range(M):
            if box[z][x][y] == 1:
                tomato.append((z, x, y, 0))

day = 0

while tomato:
    cz, cx, cy, cnt = tomato.popleft()

    for dz, dx, dy in delta:
        nz, nx, ny = cz+dz, cx+dx, cy+dy

        if 0 <= nz < H and 0 <= nx < N and 0 <= ny < M:
            if box[nz][nx][ny] == 0:
                box[nz][nx][ny] = 1
                tomato.append((nz, nx, ny, cnt+1))

    day = cnt

for z in range(H):
    for x in range(N):
        if 0 in box[z][x]:
            print(-1)
            sys.exit()

print(day)