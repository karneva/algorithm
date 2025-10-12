# codetree 숫자의 순차적 이동 dong 강사님 코드

n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# 8방향: 좌상, 상, 우상, 우, 우하, 하, 좌하, 좌  (동률 시 이 우선순위)
dy = [-1, -1, -1,  0,  1,  1,  1,  0]
dx = [-1,  0,  1,  1,  1,  0, -1, -1]

def in_range(y, x):
    return 0 <= y < n and 0 <= x < n

# 숫자 -> 현재 좌표 캐싱(성능 개선)
pos = [(-1, -1)] * (n * n + 1)
for y in range(n):
    for x in range(n):
        pos[grid[y][x]] = (y, x)

def get_best_neighbor(y, x):
    """인접 8칸 중 값이 가장 큰 칸 좌표 반환(경계 밖 제외).
       동률이면 dy/dx 배열 순서 우선."""
    best_val = -1
    by, bx = y, x
    for k in range(8):
        ny, nx = y + dy[k], x + dx[k]
        if not in_range(ny, nx):
            continue
        val = grid[ny][nx]
        if val > best_val:
            best_val = val
            by, bx = ny, nx
    return by, bx

def swap(y, x, ny, nx):
    """(y,x) <-> (ny,nx) 스왑 + pos 갱신"""
    a, b = grid[y][x], grid[ny][nx]
    grid[y][x], grid[ny][nx] = b, a
    pos[a], pos[b] = (ny, nx), (y, x)

for _ in range(m):
    for target in range(1, n * n + 1):
        y, x = pos[target]
        ny, nx = get_best_neighbor(y, x)
        if (ny, nx) != (y, x):
            swap(y, x, ny, nx)

for row in grid:
    print(*row)

'''
input
4 1
15 13 1 11
4 8 3 5
2 12 16 7
14 6 9 10
output
4 1 13 11
8 12 5 7
6 15 3 9
2 14 16 10

input
4 2
15 13 1 11
4 8 3 5
2 12 16 7
14 6 9 10
output
13 4 1 9
12 15 7 11
14 2 5 16
6 8 3 10
'''