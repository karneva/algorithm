# SWEA 4836 색칠하기

for t in range(1, int(input())+1):
    N = int(input())
    brush = [list(map(int, input().split())) for _ in range(N)]
    paint = [[0]*10 for _ in range(10)]

    violet = 0
    for b in range(N):
        for x in range(brush[b][0], brush[b][2]+1):
            for y in range(brush[b][1], brush[b][3]+1):
                paint[x][y] += brush[b][-1]

                if paint[x][y] == 3:
                    violet += 1

    print(f'#{t}', violet)