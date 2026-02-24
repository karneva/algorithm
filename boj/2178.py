# 백준 2178번: 미로 탐색

from collections import deque

N, M = map(int, input().split())

field = [list(map(int, input().strip())) for _ in range(N)]

delta = [(1, 0), (0, 1), (-1, 0), (0, -1)]

sx, sy, ex, ey = 0, 0, N-1, M-1

queue = deque([(sx, sy)])

while queue:
    x, y = queue.popleft()

    for dx, dy in delta:
        nx, ny = x+dx, y+dy

        if 0 <= nx < N and 0 <= ny < M and field[nx][ny] == 1:
            queue.append((nx, ny))
            field[nx][ny] = field[x][y] + 1

print(field[ex][ey])
