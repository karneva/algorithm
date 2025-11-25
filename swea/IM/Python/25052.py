# SWEA 25052 등산로

def bfs(n):
    if n == 2:
        return
    global result
    queue = []
    queue.append(num_index[n])

    delta = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    answer = 1
    while queue:
        cur_i, cur_j = queue.pop()
        max_length = 0
        next_i, next_j = 0, 0
        for di, dj in delta:
            ni = cur_i + di
            nj = cur_j + dj

            if 0 <= ni < N and 0 <= nj < N:
                load = mountain[cur_i][cur_j] - mountain[ni][nj]
                if load > max_length:
                    max_length = load
                    next_i, next_j = ni, nj

        if max_length == 0:
            result.append(answer)
            break

        queue.append((next_i, next_j))
        answer += 1

    bfs(n-1)

T = int(input())

for t in range(1, T+1):
    N = int(input())
    mountain = [list(map(int, input().split())) for _ in range(N)]

    start = N**2
    num_index = [[0, 0] for _ in range(N**2+1)]
    k = 2
    while k < N**2 + 1:
        for i in range(N):
            for j in range(N):
                if mountain[i][j] == k:
                    num_index[k] = [i, j]
                    k += 1
    result = []
    bfs(start)
    print(f'#{t}', max(result))