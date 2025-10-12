# codetree day12 나이트 dong 강사님 코드

from collections import deque

n = int(input())
r1, c1, r2, c2 = map(int, input().split())

q = deque()
dys = [-2, -1, 1, 2, 2, 1, -1, -2]
dxs = [1, 2, 2, 1, -1, -2, -2, -1]
visited = [
    [-1 for _ in range(n)]
    for _ in range(n)
]

def in_range(y, x):
    return 0 <= y < n and 0 <= x < n

def bfs():
    q.append((r1 - 1, c1 - 1))
    visited[r1 - 1][c1 - 1] = 0

    while q:
    # 꺼내고
        y, x = q.popleft()

    # 주위 탐색해서 넣고
        for i in range(8):
            ny = y + dys[i]
            nx = x + dxs[i]

            if not in_range(ny, nx):
                continue
            if visited[ny][nx] >= 0:
                continue

            visited[ny][nx] = visited[y][x] + 1
            q.append((ny, nx))

bfs()

print(visited[r2 - 1][c2 - 1])

'''
input
5
3 3 3 2
output
3

input
3
3 3 1 1
output
4
'''