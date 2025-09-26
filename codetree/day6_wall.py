dys = { 'U': -1, 'D': 1, 'R': 0, 'L': 0 }
dxs = { 'U': 0, 'D': 0, 'R': 1, 'L': -1 }

def in_range(y, x, N):
    return 0 <= y < N and 0 <= x < N

def flip(dir):
    if dir == 'U':
        return 'D'
    if dir == 'D':
        return 'U'
    if dir == 'L':
        return 'R'
    if dir == 'R':
        return 'L'
    raise Exception

def simulate(N, marbles):
    marble_cnts = [[0] * N for _ in range(N)]

for y in range(N):
    for x in range(N):
        if marbles[y][x] == 0:
            continue

dir = marbles[y][x]
ny = y + dys[dir]
nx = x + dxs[dir]

if not in_range(ny, nx, N):
marble_cnts[y][x] += 1
else:
marble_cnts[ny][nx] += 1

for y in range(N):
for x in range(N):
if marble_cnts[y][x] >= 2:
marble_cnts[y][x] = 0

tmp_marbles = [[0] * N for _ in range(N)]

for y in range(N):
for x in range(N):
if marbles[y][x] == 0:
continue

dir = marbles[y][x]
ny = y + dys[dir]
nx = x + dxs[dir]

if not in_range(ny, nx, N):
ny = y
nx = x
dir = flip(dir)

if marble_cnts[ny][nx] == 1:
tmp_marbles[ny][nx] = dir

for y in range(N):
for x in range(N):
marbles[y][x] = tmp_marbles[y][x]

def print_cnt(N, marbles):
cnt = 0

for y in range(N):
for x in range(N):
if marbles[y][x] != 0:
cnt += 1

print(cnt)

def print_marbles(N, marbles):
for y in range(N):
for x in range(N):
print(marbles[y][x], end=" ")
print()
print()

T = int(input())

for _ in range(T):
N, M = map(int, input().split())
marbles = [[0] * N for _ in range(N)]
for _ in range(M):
y, x, d = input().split()
marbles[int(y) - 1][int(x) - 1] = d

for _ in range(100):
simulate(N, marbles)
print_cnt(N, marbles)
