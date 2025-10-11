# codetree 1차원 바람 dong 강사님 코드

n, m, q = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

def move_possible(r1, r2):
    for i in range(m):
        if grid[r1][i] == grid[r2][i]:
            return True
    return False

def move(r, d):
    if d == 'L':
        tmp = grid[r][-1]
        for i in range(m - 1, 0, -1):
            grid[r][i] = grid[r][i - 1]
        grid[r][0] = tmp
    else:
        tmp = grid[r][0]
        for i in range(0, m - 1):
            grid[r][i] = grid[r][i + 1]
        grid[r][m - 1] = tmp
    return 'L' if d == 'R' else 'R'

def simulate(r, d):
    nd_up = move(r, d)
    nd_down = nd_up

    for i in range(r - 1, -1, -1):
        if move_possible(i, i + 1):
            nd_up = move(i, nd_up)
        else:
            break

    for i in range(r + 1, n):
        if move_possible(i, i - 1):
            nd_down = move(i, nd_down)
        else:
            break

for _ in range(q):
    r, dir = input().split()
    r = int(r) - 1
    simulate(r, dir)

for i in range(n):
    print(*grid[i])



'''
input
6 5 1
1 5 6 7 3
5 3 2 5 4
6 4 5 2 5
2 6 1 0 5
5 1 2 1 6
4 2 5 2 8
3 L
output
1 5 6 7 3
3 2 5 4 5
5 6 4 5 2
6 1 0 5 2
6 5 1 2 1
2 5 2 8 4

input
3 3 2
1 2 3
3 2 1
3 3 3
3 L
1 L
output
2 3 1
1 3 2
3 3 3
'''