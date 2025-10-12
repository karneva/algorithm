# codetree 벽 짚고 미로 탈출하기

N = int(input())
x, y = map(int, input().split())
arr = [list(input()) for _ in range(N)]

# 0:E, 1:S, 2:W, 3:N (시계방향)
delta = [[0, 1], [1, 0], [0, -1], [-1, 0]]

cur_i, cur_j = x - 1, y - 1
dir = 0  # 시작 방향(동쪽).
time = 0

visited = set()
visited.add((cur_i, cur_j, dir))

def in_range(i, j):
    return 0 <= i < N and 0 <= j < N

while True:
    right_dir = (dir + 1) % 4       # 오른쪽
    left_dir = (dir + 3) % 4        # 왼쪽
    fi, fj = cur_i + delta[dir][0],       cur_j + delta[dir][1]        # 정면
    ri, rj = cur_i + delta[right_dir][0], cur_j + delta[right_dir][1]  # 오른쪽

    moved = False

    # 1) 오른쪽이 비어 있으면 오른쪽으로 회전 + 전진
    if in_range(ri, rj) and arr[ri][rj] != '#':
        ndir = right_dir
        ni, nj = cur_i + delta[ndir][0], cur_j + delta[ndir][1]
        # 한 걸음 나가면서 탈출?
        if not in_range(ni, nj):
            time += 1
            break
        # 사이클 체크는 add 전에!
        if (ni, nj, ndir) in visited:
            time = -1
            break
        visited.add((ni, nj, ndir))
        cur_i, cur_j, dir = ni, nj, ndir
        time += 1
        moved = True

    # 2) 오른쪽이 막혀 있으면, 정면이 비어 있으면 직진
    if not moved:
        if in_range(fi, fj) and arr[fi][fj] != '#':
            ndir = dir
            ni, nj = fi, fj
            if not in_range(ni, nj):
                time += 1
                break
            if (ni, nj, ndir) in visited:
                time = -1
                break
            visited.add((ni, nj, ndir))
            cur_i, cur_j, dir = ni, nj, ndir
            time += 1
            moved = True

    # 3) 정면도 막혀 있으면 왼쪽으로 회전만 하고(이동 없음) 다음 루프
    if not moved:
        dir = left_dir
        # 현재 상태(좌회전 후)가 이미 방문 상태라면 무한 회전 가능성이 있으니 체크
        if (cur_i, cur_j, dir) in visited:
            time = -1
            break
        visited.add((cur_i, cur_j, dir))

print(time)

'''
input
3
1 1
.#.
#..
...
output
1

input
3
1 1
...
##.
...
output
7

input
3
1 1
...
#..
...
output
5

input
3
1 2
...
.#.
...
output
-1
'''