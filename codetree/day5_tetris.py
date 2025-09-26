import sys
sys.stdin = open('input.txt')

n, m, k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

i = 0
k -= 1
while True:
    if 1 not in grid[i][k:k+m]:
        if i == n-1 or 1 in grid[i+1][k:k+m]:
            for j in range(m):
                grid[i][k+j] = 1

            break
    i += 1

for g in grid:
    print(*g)