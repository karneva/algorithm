# SWEA 1979 어디에 단어가 들어갈 수 있을까

def insert_word(arr):
    # i, j 좌표를 받아 1의 개수를 카운트
    count = 0
    for i in range(N):
        cnt = 0
        for j in range(N):
            if arr[i][j] == 1:
                cnt += 1
            else:
                if cnt == M:
                    count += 1
                cnt = 0
        if cnt == M:
            count += 1
    return count

T = int(input())

for t in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    arr_T = list(zip(*arr))
    ans1 = insert_word(arr)
    ans2 = insert_word(arr_T)
    print(f'#{t}', ans1+ans2)