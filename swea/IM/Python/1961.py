# SWEA 1961 숫자 배열 회전

def round_arr(arr):
    arr_r = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            arr_r[j][N-i-1] = arr[i][j]
    return arr_r
 
T = int(input())
 
for t in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
 
    arr_90 = round_arr(arr)
    arr_180 = round_arr(arr_90)
    arr_270 = round_arr(arr_180)
 
    print(f'#{t}')
    for i in range(N):
        print(*arr_90[i], sep='', end=' ')
        print(*arr_180[i], sep='', end=' ')
        print(*arr_270[i], sep='')
