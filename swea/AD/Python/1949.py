# SWEA 1949 등산로 조성

def find_root(cur_h, cur_i, cur_j, cnt):
    global use_drill, result

    # 현재 높이가 0보다 작거나 같다면 더 이상 어디 못가니 리턴
    if cur_h <= 0:
        result = max(cnt, result)
        return

    for di, dj in delta:
        ni = cur_i + di
        nj = cur_j + dj

        if 0 > ni or N <= ni or 0 > nj or N <= nj:
            continue
 
        for i in range(1, K+1):
            # 만약 이미 팠거나 방문한 곳이라면 중단
            if use_drill or visited[ni][nj]:
                break
            after_drill = mountain[ni][nj] - i
            # 만약 팠는데 현재 높이가 깎은 곳보다 낮아지거나 0이 돼버리면 continue
            if cur_h <= after_drill or after_drill < 0:
                continue
            use_drill = True
            visited[ni][nj] = True
            find_root(after_drill, ni, nj, cnt+1)
            use_drill = False
            visited[ni][nj] = False
 
        # 만약 현재 높이보다 다음 높이가 같거나 높으면 continue
        if cur_h <= mountain[ni][nj]:
            continue
        visited[ni][nj] = True
        find_root(mountain[ni][nj], ni, nj, cnt+1)
        visited[ni][nj] = False

    result = max(cnt, result)

T = int(input())

for t in range(1, T+1):
    N, K = map(int, input().split())
    mountain = [list(map(int, input().split())) for _ in range(N)]
    visited = [[False]*N for _ in range(N)]

    # 가장 높은 봉우리 위치 계산
    max_bong = 0

    for i in range(N):
        max_bong = max(max_bong, max(mountain[i]))

    use_drill = False
    delta = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    result = 0

    for i in range(N):
        for j in range(N):
            # 가장 높은 봉우리 일 때 루트 찾는 함수 시작
            if mountain[i][j] == max_bong:
                visited = [[False] * N for _ in range(N)]
                visited[i][j] = True
                find_root(max_bong, i, j, 1)

    print(f'#{t}', result)