import sys
sys.stdin = open('input.txt')

n, m, t = map(int, input().split())

# Create n x n grid
a = [list(map(int, input().split())) for _ in range(n)]

# Get m marble positions
prev_pos = []
for _ in range(m):
    r, c = map(int, input().split())
    prev_pos.append((r-1, c-1))

delta = [[-1, 0], [1, 0], [0, -1], [0, 1]]

i = 0

while i < t:
    next_pos = []
    for j in range(len(prev_pos)):
        max_bead = 0
        max_i, max_j = 0, 0
        for di, dj in delta:
            ni, nj = prev_pos[j][0] + di, prev_pos[j][1] + dj

            if 0 <= ni < n and 0 <= nj < n:
                if a[ni][nj] > max_bead:
                    max_bead = a[ni][nj]
                    max_i, max_j = ni, nj
        next_pos.append((max_i, max_j))

    if len(set(prev_pos) & set(next_pos)) == 2:
        prev_pos = list(set(next_pos) - set(prev_pos))
    else:
        prev_pos = next_pos[:]

    i += 1

print(len(prev_pos))