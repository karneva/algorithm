# SWEA Magnetic

for t in range(1, 11):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
    # 회전시킨 모양이 보기 편하니까 회전
    arr_T = [list(col) for col in zip(*arr)]

    count = 0
    for i in range(100):
        stack = []
        for j in range(100):
            if arr_T[i][j] == 1:
                stack.append(1)
            elif arr_T[i][j] == 2 and stack:
                count += 1
                stack.clear()

    print(f'#{t}', count)