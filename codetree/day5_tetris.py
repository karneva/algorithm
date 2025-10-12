# codetree 떨어지는 1자 블록

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

'''
input
4 3 1
0 0 0 0
0 0 0 1
1 0 0 1
1 1 1 1
output
0 0 0 0
1 1 1 1
1 0 0 1
1 1 1 1

input
4 2 2
0 0 0 0
0 0 0 1
1 0 0 1
1 1 1 1
output
0 0 0 0
0 0 0 1
1 1 1 1
1 1 1 1
'''