# codetree 십자 모양 폭발

n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
r, c = map(int, input().split())

r -= 1
c -= 1

delta = [[0, 1], [1, 0], [0, -1], [-1, 0]]

bomb = grid[r][c]

for di, dj in delta:
    ni, nj = r, c
    for _ in range(bomb-1):
        ni += di
        nj += dj

        if 0 <= ni < n and 0 <= nj < n:
            grid[ni][nj] = 0

grid[r][c] = 0

cnt = 0
while cnt < n:
    for i in range(n-1):
        for j in range(n):
            if grid[i+1][j] == 0:
                grid[i][j], grid[i+1][j] = grid[i+1][j], grid[i][j]
    cnt += 1

for g in grid:
    print(*g)
    
'''
input
4
1 2 4 3
3 2 2 3
3 1 6 2
4 5 4 4
2 3
output
1 0 0 0
3 2 0 3
3 1 0 2
4 5 4 4

input
4
1 2 4 3
3 2 2 3
3 1 6 2
4 5 4 4
3 3
output
0 0 0 0
1 2 0 3
3 2 0 3
4 5 0 4
'''