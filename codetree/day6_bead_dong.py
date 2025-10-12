# codetree 숫자가 가장 큰 인접한 곳으로 동시에 이동 dong 강사님 코드

n, m, t = map(int, input().split())
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]

# 현재 marbles의 위치정보
marbles = [[0] * n for _ in range(n)]

for _ in range(m):
    r, c = map(int, input().split())
    r, c = r - 1, c - 1
    marbles[r][c] = 1

# 상, 하, 좌, 우 (동점 시 이 순서로 우선)
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

def in_range(y, x):
    return 0 <= y < n and 0 <= x < n

def get_next_pos(y, x):
    # 인접한 상하좌우 중 가장 큰 숫자의 좌표를 리턴
    best_val = -10**18
    ny, nx = y, x  # 혹시 모두 막힌 경우 대비(문제 조건상 항상 이동 가능)
    for k in range(4):
        ty, tx = y + dy[k], x + dx[k]
        if not in_range(ty, tx):
            continue
        val = grid[ty][tx]
        if val > best_val:
            best_val = val
            ny, nx = ty, tx
    return ny, nx

def simulate():
    # 격자에 있는 모든 구슬들을 동시에 이동
    next_marbles = [[0] * n for _ in range(n)]

    for y in range(n):
        for x in range(n):
            if marbles[y][x] == 0:
                continue
            ny, nx = get_next_pos(y, x)
            next_marbles[ny][nx] += marbles[y][x]  # (여러 개가 같은 칸에 있어도 모두 이동)

    # 충돌 소멸
    for y in range(n):
        for x in range(n):
            if next_marbles[y][x] >= 2:
                next_marbles[y][x] = 0

    # 상태 갱신
    for y in range(n):
        for x in range(n):
            marbles[y][x] = next_marbles[y][x]

for _ in range(t):
    simulate()

print(sum(sum(row) for row in marbles))

'''
marbles에서
1
의
개수를
찾아서
출력.
'''

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