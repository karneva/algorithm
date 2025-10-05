# codetree 1이 3개 이상 있는 위치

n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

delta = [[0, 1], [0, -1], [1, 0], [-1, 0]]
cnt = 0
for i in range(n):
    for j in range(n):
        one_cnt = 0
        for di, dj in delta:
            ni = i + di
            nj = j + dj
            if 0 <= ni < n and 0 <= nj < n and grid[ni][nj] == 1:
                one_cnt += 1
        if one_cnt >= 3:
            cnt += 1

print(cnt)

'''
input
4
0 1 0 1
0 0 1 1
0 1 0 1
0 0 1 0
output
4
'''