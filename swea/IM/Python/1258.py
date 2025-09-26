# SWEA 1258 행렬찾기

def find_matrix(x, y, arr):
    dx, dy = 1, 1

    while arr[x][y + dy] != 0:
        dy += 1
    while arr[x + dx][y] != 0:
        dx += 1

    for sx in range(x, x + dx):
        for sy in range(y, y + dy):
            arr[sx][sy] = 0
    return dx, dy

for t in range(1, int(input())+1):
    N = int(input())
    warehouse = [list(map(int, input().split())) for _ in range(N)]

    ret = []
    lst = []
    for i in range(N):
        for j in range(N):
            if warehouse[i][j] != 0:
                r, c = find_matrix(i, j, warehouse)
                lst.append([r, c])
    lst = sorted(lst, key=lambda x: (x[0] * x[1], x[0]))

    for temp in lst:
        ret.append(temp[0])
        ret.append(temp[1])
    print(f"#{t} {len(lst)}", *ret)