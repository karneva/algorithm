# SWEA 1209 SUM

for t in range(1, 11):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]

    col = max([sum(cols) for cols in arr])
    row = max([sum(rows) for rows in zip(*arr)])
    r_ = sum([arr[x][x] for x in range(100)])
    l_ = sum([arr[x][99-x] for x in range(100)])

    print(f'#{N}', max(col, row, r_, l_))