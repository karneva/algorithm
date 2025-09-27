# SWEA 1949 등산로 조성 GPT 코드 수정 부분

def find_root(i, j, cur_h, cnt, drilled):
    global result

    result = max(result, cnt)

    for dx, dy in delta:
        ni, nj = i + dx, j + dy

        if not (0 <= ni < N and 0 <= nj < N):
            continue
        if visited[ni][nj]:
            continue

        next_h = mountain[ni][nj]

        # Case 1: 그냥 갈 수 있는 경우
        if next_h < cur_h:
            visited[ni][nj] = True
            find_root(ni, nj, next_h, cnt + 1, drilled)
            visited[ni][nj] = False

        # Case 2: 드릴 사용 가능
        elif not drilled and next_h - K < cur_h:
            for cut in range(1, K + 1):
                cut_h = next_h - cut
                if cut_h < 0 or cut_h >= cur_h:
                    continue
                visited[ni][nj] = True
                find_root(ni, nj, cut_h, cnt + 1, True)
                visited[ni][nj] = False

T = int(input())
for t in range(1, T + 1):
    N, K = map(int, input().split())
    mountain = [list(map(int, input().split())) for _ in range(N)]

    max_h = max(max(row) for row in mountain)
    start_points = [(i, j) for i in range(N) for j in range(N) if mountain[i][j] == max_h]

    result = 0
    delta = [(-1,0), (1,0), (0,-1), (0,1)]

    for i, j in start_points:
        visited = [[False] * N for _ in range(N)]
        visited[i][j] = True
        find_root(i, j, mountain[i][j], 1, False)

    print(f"#{t} {result}")
