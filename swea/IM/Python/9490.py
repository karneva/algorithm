# SWEA 9490 풍선팡

for t in range(1, int(input())+1):
    N, M = map(int, input().split())
    balloon = [list(map(int, input().split())) for _ in range(N)]

    delta = [[0, 1], [1, 0], [0, -1], [-1, 0]]

    max_Pang = 0
    for i in range(N):
        for j in range(M):
            Pang = balloon[i][j]
            for di, dj in delta:
                ni, nj = i, j
                for _ in range(balloon[i][j]):
                    ni += di
                    nj += dj
                    if 0 <= ni < N and 0 <= nj < M:
                        Pang += balloon[ni][nj]

            if max_Pang < Pang:
                max_Pang = Pang
    print(f'#{t}', max_Pang)