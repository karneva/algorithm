import sys
sys.stdin = open('input.txt')

def solve(cur_i, cur_j):
    print(arr[cur_i][cur_j], end=' ')
    for di, dj in delta:
        ni = cur_i + di
        nj = cur_j + dj

        if 0 <= ni < n and 0 <= nj < n:
            if arr[ni][nj] > arr[cur_i][cur_j]:
                solve(ni, nj)
                break

n, r, c = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

delta = [[-1, 0], [1, 0], [0, -1], [0, 1]]

solve(r-1, c-1)
print()