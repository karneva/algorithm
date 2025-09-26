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


def get_next_pos(y, x):
    # dx-dy 테크닉을 이용해서
    # 인접한 상하좌우 중 가장 큰 숫자의 좌표를 리턴

    return ny, nx


def simulate():
    # 격자에 있는 모든 구슬들을 이동시킨다.

    # 다음 marbles의 위치정보
    next_marbles = [[0] * n for _ in range(n)]

    for y in range(n):
        for x in range(n):
            if marbles[y][x] == 0:
                continue

            # 구슬의 움직임을 다룬다.
            ny, nx = get_next_pos(y, x)
            next_marbles[ny][nx] += 1

    for y in range(n):
        for x in range(n):
            # 충돌이 발생했다.
            if next_marbles[y][x] >= 2:
                next_marbles[y][x] = 0

    for y in range(n):
        for x in range(n):
            marbles[y][x] = next_marbles[y][x]


for _ in range(T):
    simulate()
'''
marbles에서
1
의
개수를
찾아서
출력.
'''