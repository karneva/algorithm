# codetree 숫자가 가장 큰 인접한 곳으로 동시에 이동

n, m, t = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

cnt = [[0]*n for _ in range(n)]
for _ in range(m):
    r, c = map(int, input().split())
    cnt[r-1][c-1] += 1

DIRS = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

for _ in range(t):
    next_cnt = [[0]*n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            k = cnt[i][j]
            if k == 0:
                continue

            best_val = -10**18
            nx, ny = i, j
            for dx, dy in DIRS:
                xi, yj = i + dx, j + dy
                if in_range(xi, yj) and grid[xi][yj] > best_val:
                    best_val = grid[xi][yj]
                    nx, ny = xi, yj

            next_cnt[nx][ny] += k

    for i in range(n):
        for j in range(n):
            if next_cnt[i][j] >= 2:
                next_cnt[i][j] = 0

    cnt = next_cnt

ans = sum(cnt[i][j] for i in range(n) for j in range(n))
print(ans)

'''
input
4 3 1
1 2 2 3
3 5 10 15
3 8 11 2
4 5 4 4
2 2
3 4
4 2
output
3

input
4 3 3
1 2 2 3
3 5 10 15
3 8 11 2
4 5 4 4
2 2
3 4
4 2
output
1
'''