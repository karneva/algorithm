# codetree 숫자가 더 큰 인접한 곳으로 이동

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

'''
input
4 2 2
1 2 2 3
3 5 10 15
3 8 11 2
4 5 4 4
output
5 8 11

input
4 1 1
1 2 2 3
3 5 10 15
3 8 11 2
4 5 4 4
output
1 3 5 8 11
'''