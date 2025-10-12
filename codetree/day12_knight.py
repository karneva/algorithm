# codetree day12 나이트

from collections import deque

# 입력
n = int(input().strip())
sr, sc, tr, tc = map(int, input().split())

# 1-indexed -> 0-indexed
sr -= 1; sc -= 1; tr -= 1; tc -= 1

# 나이트 8방향
DR = (2,  2,  1,  1, -1, -1, -2, -2)
DC = (1, -1,  2, -2,  2, -2,  1, -1)

def in_range(r, c):
    return 0 <= r < n and 0 <= c < n

# BFS: dist[r][c] = (sr,sc)에서 (r,c)까지 최소 이동 횟수
dist = [[-1]*n for _ in range(n)]
dq = deque([(sr, sc)])
dist[sr][sc] = 0

while dq:
    r, c = dq.popleft()
    if (r, c) == (tr, tc):
        print(dist[r][c])
        break
    for k in range(8):
        nr, nc = r + DR[k], c + DC[k]
        if in_range(nr, nc) and dist[nr][nc] == -1:
            dist[nr][nc] = dist[r][c] + 1
            dq.append((nr, nc))
else:
    # 정상적인 체스판에선 항상 도달 가능하지만, 안전하게 처리
    print(-1)

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