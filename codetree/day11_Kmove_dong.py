# codetree K번 최댓값으로 이동하기 dong 강사님 코드

from collections import deque

n, k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
curr_r, curr_c = map(int, input().split())
curr_r -= 1
curr_c -= 1

# 4방향
DR = (-1, 0, 1, 0)
DC = (0, 1, 0, -1)

def in_range(r, c):
    return 0 <= r < n and 0 <= c < n

# 방문 체크: 스탬프 기법(visited를 매번 초기화하지 않음)
visited = [[0]*n for _ in range(n)]
stamp = 0

def bfs(sr, sc):
    """sr,sc에서 시작하여 grid[sr][sc]보다 작은 값들만 4방향으로 확장"""
    vlim = grid[sr][sc]
    q = deque([(sr, sc)])
    visited[sr][sc] = stamp

    while q:
        r, c = q.popleft()
        for d in range(4):
            nr, nc = r + DR[d], c + DC[d]
            if not in_range(nr, nc):
                continue
            if visited[nr][nc] == stamp:
                continue
            if grid[nr][nc] >= vlim:
                continue
            visited[nr][nc] = stamp
            q.append((nr, nc))

def get_next_pos(sr, sc):
    """visited==stamp 중에서 (sr,sc) 제외, 값 최대 → (행,열) 최소"""
    best_val = None
    best_r = best_c = -1
    for r in range(n):
        rowv = visited[r]
        for c in range(n):
            if (r == sr and c == sc) or rowv[c] != stamp:
                continue
            v = grid[r][c]
            if best_val is None or v > best_val or (v == best_val and (r < best_r or (r == best_r and c < best_c))):
                best_val, best_r, best_c = v, r, c
    if best_val is None:
        return None
    return best_r, best_c

for _ in range(k):
    stamp += 1
    bfs(curr_r, curr_c)

    nxt = get_next_pos(curr_r, curr_c)
    if nxt is None:       # 이동 불가
        break
    curr_r, curr_c = nxt  # 이동

print(curr_r + 1, curr_c + 1)

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
