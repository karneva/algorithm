# codetree 벽이 있는 충돌 실험 dong 강사님 코드

dys = { 'U': -1, 'D': 1, 'R': 0, 'L': 0 }
dxs = { 'U': 0, 'D': 0, 'R': 1, 'L': -1 }

def in_range(y, x, N):
    return 0 <= y < N and 0 <= x < N

def flip(dir):
    if dir == 'U': return 'D'
    if dir == 'D': return 'U'
    if dir == 'L': return 'R'
    if dir == 'R': return 'L'
    raise Exception

def simulate(N, marbles):
    # 1) 목적지 카운트(동시 이동 위해 목적지별 개수 세기)
    marble_cnts = [[0] * N for _ in range(N)]
    for y in range(N):
        for x in range(N):
            if marbles[y][x] == 0:
                continue
            dir = marbles[y][x]
            ny = y + dys[dir]
            nx = x + dxs[dir]
            if not in_range(ny, nx, N):
                # 벽: 이동하지 않고 현 위치에 남는다(목적지는 현재 칸)
                marble_cnts[y][x] += 1
            else:
                marble_cnts[ny][nx] += 1

    # 2) 충돌 소멸(2개 이상 모인 칸은 모두 사라짐)
    for y in range(N):
        for x in range(N):
            if marble_cnts[y][x] >= 2:
                marble_cnts[y][x] = 0

    # 3) 실제 배치 갱신(방향 반전 포함)
    tmp_marbles = [[0] * N for _ in range(N)]
    for y in range(N):
        for x in range(N):
            if marbles[y][x] == 0:
                continue
            dir = marbles[y][x]
            ny = y + dys[dir]
            nx = x + dxs[dir]
            if not in_range(ny, nx, N):
                # 벽이면 제자리 + 방향 반전
                ny, nx = y, x
                dir = flip(dir)

            # 목적지에 1개만 도착하는 경우에만 살아남아 배치
            if marble_cnts[ny][nx] == 1:
                tmp_marbles[ny][nx] = dir

    # 4) 상태 적용
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

    for _ in range(2*N):
        simulate(N, marbles)
    print_cnt(N, marbles)

'''
input
1
4 5
1 2 L
2 3 U
3 1 R
3 4 D
4 2 U
output
1

input
3
2 2
1 1 L
2 2 R
2 2
1 1 D
2 2 R
2 2
1 1 L
1 2 R
output
2
0
2
'''