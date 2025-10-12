# codetree 숫자의 순차적 이동

def solve():
    n, m = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(n)]

    pos = [(-1, -1)] * (n * n + 1)
    for i in range(n):
        for j in range(n):
            pos[a[i][j]] = (i, j)

    dirs = [(-1, -1), (-1, 0), (-1, 1), (0, 1),
            (1, 1), (1, 0), (1, -1), (0, -1)]

    def in_range(x, y):
        return 0 <= x < n and 0 <= y < n

    for _ in range(m):
        for num in range(1, n * n + 1):
            x, y = pos[num]
            best = None
            for dx, dy in dirs:
                nx, ny = x + dx, y + dy
                if in_range(nx, ny):
                    if best is None or a[nx][ny] > best[0]:
                        best = (a[nx][ny], nx, ny)

            if best is None:
                continue

            _, nx, ny = best
            other = a[nx][ny]
            a[x][y], a[nx][ny] = a[nx][ny], a[x][y]
            # 위치 갱신
            pos[num] = (nx, ny)
            pos[other] = (x, y)

    for i in range(n):
        print(*a[i])

solve()

'''
input
4 1
15 13 1 11
4 8 3 5
2 12 16 7
14 6 9 10
output
4 1 13 11
8 12 5 7
6 15 3 9
2 14 16 10

input
4 2
15 13 1 11
4 8 3 5
2 12 16 7
14 6 9 10
output
13 4 1 9
12 15 7 11
14 2 5 16
6 8 3 10
'''