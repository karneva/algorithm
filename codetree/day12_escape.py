# codetree day12 최소 경로로 탈출 하기

from collections import deque

n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# 통로가 아니면 바로 불가능
if grid[0][0] == 0 or grid[n-1][m-1] == 0:
    print(-1)
    sys.exit(0)

# 방문 배열을 "거리"로 사용 (-1 = 미방문)
dist = [[-1]*m for _ in range(n)]

DR = (-1, 0, 1, 0)
DC = ( 0, 1, 0,-1)

def in_range(r, c):
    return 0 <= r < n and 0 <= c < m

def bfs():
    dq = deque([(0, 0)])
    dist[0][0] = 0

    while dq:
        r, c = dq.popleft()
        # 목표에 도달하면 즉시 반환 (조기 종료)
        if r == n-1 and c == m-1:
            return dist[r][c]

        for d in range(4):
            nr, nc = r + DR[d], c + DC[d]
            if not in_range(nr, nc):      # 격자 밖
                continue
            if grid[nr][nc] == 0:         # 벽
                continue
            if dist[nr][nc] != -1:        # 이미 방문
                continue

            dist[nr][nc] = dist[r][c] + 1
            dq.append((nr, nc))

    return -1  # 도달 불가

ans = bfs()
print(ans)

'''
input
5 5
1 0 1 1 1
1 0 1 0 1
1 0 1 1 1
1 0 1 0 1
1 1 1 0 1
output
12

input
5 5
1 1 1 1 1
1 0 1 0 1
1 1 1 1 1
1 0 1 0 1
1 1 1 0 1
output
8
'''