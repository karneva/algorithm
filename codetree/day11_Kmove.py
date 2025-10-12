# codetree K번 최댓값으로 이동하기

from collections import deque

n, k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
r, c = map(int, input().split())
r -= 1; c -= 1

DR = (-1, 0, 1, 0)
DC = (0, 1, 0, -1)

def in_range(y, x):
    return 0 <= y < n and 0 <= x < n

# visited를 스탬프 방식으로 관리(턴마다 재할당 없음)
visited = [[0]*n for _ in range(n)]
stamp = 0

def bfs_pick(sr, sc):
    """sr,sc에서 시작값보다 작은 칸들만 4방향 BFS로 확장하며,
       그 중 '값 최대 → (행,열) 최소' 칸을 골라 반환. 없으면 None."""
    nonlocal stamp
    stamp += 1
    q = deque([(sr, sc)])
    visited[sr][sc] = stamp
    limit = grid[sr][sc]

    best_val = None
    best_r = best_c = -1

    while q:
        y, x = q.popleft()
        for d in range(4):
            ny, nx = y + DR[d], x + DC[d]
            if not in_range(ny, nx) or visited[ny][nx] == stamp:
                continue
            v = grid[ny][nx]
            if v >= limit:
                continue
            visited[ny][nx] = stamp
            q.append((ny, nx))
            # 후보 갱신(시작 칸 제외: 방문상 ny,nx는 항상 시작이 아님)
            if (best_val is None or
                v > best_val or
                (v == best_val and (ny < best_r or (ny == best_r and nx < best_c)))):
                best_val, best_r, best_c = v, ny, nx

    if best_val is None:
        return None
    return best_r, best_c

for _ in range(k):
    nxt = bfs_pick(r, c)
    if nxt is None:
        break
    r, c = nxt

print(r + 1, c + 1)

'''
input
4 2
1 3 2 11
4 9 6 9
2 6 9 8
1 9 10 7
4 3
output
2 3

input
4 4
1 3 2 11
4 9 6 9
2 6 9 8
1 9 10 7
4 3
output
1 2
'''
