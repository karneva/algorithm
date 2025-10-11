# codetree 행복한 수열의 개수

n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
grid_T = [list(col) for col in zip(*grid)]

cnt = 0
if m == 1:
    print(n*2)
else:
    for i in range(n):
        num_cnt, num_T_cnt = 1, 1
        for j in range(n-1):
            if grid[i][j] == grid[i][j+1]:
                num_cnt += 1
            else:
                if num_cnt >= m:
                    cnt += 1
                    break
                num_cnt = 1
        else:
            if num_cnt >= m:
                cnt += 1
        for j in range(n-1):
            if grid_T[i][j] == grid_T[i][j+1]:
                num_T_cnt += 1
            else:
                if num_T_cnt >= m:
                    cnt += 1
                    break
                num_T_cnt = 1
        else:
            if num_T_cnt >= m:
                cnt += 1

    print(cnt)
     
'''
input
3 2
1 2 2
1 3 4
1 2 3
output
2

input
3 1
1 2 3
4 5 6
7 8 8
output
6
'''