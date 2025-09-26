n, m = map(int, input().split())
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]

# 격자 안에서 Target이 위치한 좌표를 리턴
def find_pos(target):
    for y in range(n):
        for x in range(n):
            if grid[y][x] == target:
                return y, x
    # raise Exception

def swap(y, x):
    # dx, dy 테크닉을 이용해서
    # 인접한 숫자들 중 가장 큰 숫자의 좌표를 찾는다
    max_num = 0
    max_y, max_x = y, x

    for i in range(8):
        ny = y + dy[i]
        nx = x + dx[i]

        if grid[ny][nx] > max_num:
            max_num = grid[ny][nx]
            max_y, max_x = ny, nx

    grid[y][x], grid[max_y][max_x] = grid[max_y][max_x], grid[y][x]

for target in range(1, n * n + 1):
    y, x = find_pos(target)
    swap(y, x)