# 백준 2206번: 벽 부수고 이동하기

import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())

field = [list(map(int, input().strip())) for _ in range(N)]

dist = [[[0]*2 for _ in range(M)] for _ in range(N)]
dist[0][0][0] = 1

delta = [(1,0), (0,1), (-1,0), (0,-1)]

queue = deque([(0, 0, 0)])

while queue:
    x, y, smash = queue.popleft()

    if x == N-1 and y == M-1:
        print(dist[x][y][smash])
        sys.exit()

    for dx, dy in delta:
        nx, ny = x+dx, y+dy

        if 0 <= nx < N and 0 <= ny < M:
            if field[nx][ny] == 0 and dist[nx][ny][smash] == 0:
                dist[nx][ny][smash] = dist[x][y][smash] + 1
                queue.append((nx, ny, smash))
            elif field[nx][ny] == 1 and smash == 0 and dist[nx][ny][smash] == 0:
                dist[nx][ny][1] = dist[x][y][smash] + 1
                queue.append((nx, ny, 1))

print(-1)