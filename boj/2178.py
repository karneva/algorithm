# 백준 2178번: 미로 탐색

from collections import deque

N, M = map(int, input().split())

field = [list(map(int, input().strip())) for _ in range(N)]

delta = [(1, 0), (0, 1), (-1, 0), (0, -1)]

sx, sy, ex, ey = 0, 0, N-1, M-1

