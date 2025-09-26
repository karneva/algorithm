import sys
sys.stdin = open('input.txt')

def recur(grid, bomb, target_point, n, used):
    global result

    for point in range(len(target_point)):
        if not used[point]:
            used[point] = True
            r, c = target_point[point]

            for b in bomb:
                grid_copy = [col[:] for col in grid]
                for di, dj in b:
                    ni, nj = r + di, c + dj

                    if ni < 0 or ni >= n or nj < 0 or nj >= n:
                        continue

                    grid_copy[ni][nj] = 1

                recur(grid_copy, bomb, target_point, n, used)
            used[point] = False

    cnt = sum([i.count(1) for i in grid])
    result = max(result, cnt)

def find_target(n, grid):
    result = []
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 1:
                result.append((i, j))

    return result

if __name__ == "__main__":
    n = int(input())
    grid = [list(map(int, input().split())) for _ in range(n)]
    bomb = [[[-2, 0], [-1, 0], [1, 0], [2, 0]],
            [[0, 1], [1, 0], [0, -1], [-1, 0]],
            [[-1, -1], [1, -1], [-1, 1], [1, 1]]]

    result = 0
    target_point = find_target(n, grid)
    used = [False] * (len(target_point))
    recur(grid, bomb, target_point, n, used)
    print(result)