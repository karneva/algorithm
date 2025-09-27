# SWEA 1953 탈주범 검거

from collections import deque

def bfs(cur_i, cur_j, cnt):
    # 우, 하, 좌, 상 델타
    delta = [[0, 1], [1, 0], [0, -1], [-1, 0]]

    # 우, 하, 좌, 상
    structure = {
        1: [1, 1, 1, 1],
        2: [0, 1, 0, 1],
        3: [1, 0, 1, 0],
        4: [1, 0, 0, 1],
        5: [1, 1, 0, 0],
        6: [0, 1, 1, 0],
        7: [0, 0, 1, 1]
    }

    queue = deque([])
    queue.append((cur_i, cur_j, cnt))
    visited = [[0] * M for _ in range(N)]
    visited[cur_i][cur_j] = 1

    while queue:
        i, j, c = queue.popleft()
        if c == L:
            continue

        for d in range(4):
            # 현재 위치의 파이프가 연결되는 방향을 찾는다
            if structure[arr[i][j]][d] == 1:
                di, dj = delta[d]
                ni, nj = i + di, j + dj
                if 0 <= ni < N and 0 <= nj < M:
                    # 현재 위치의 파이프가 무엇인지 찾느다
                    pipe = arr[ni][nj]
                    # 파이프가 있고 방문하지 않았으며 현재 위치와 연결되어 있다면 이동 가능
                    if pipe and visited[ni][nj] == 0 and structure[pipe][(d+2)%4] == 1:
                        # 방문 표시 및 큐 삽입
                        visited[ni][nj] = 1
                        queue.append((ni, nj, c+1))

    return sum([i.count(1) for i in visited])

T = int(input())

for t in range(1, T+1):
    N, M, R, C, L = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    print(f'#{t}', bfs(R, C, 1))