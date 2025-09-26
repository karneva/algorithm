# SWEA 2805 농작물 수확하기

for t in range(1, int(input()) + 1):
    N = int(input())
    field = [list(map(int, input())) for _ in range(N)]

    i = 0
    # 가운데 줄은 미리 더해놓기
    total = sum(field[N//2][:])
    while i < N//2:
        total += sum(field[i][N//2-i:N//2+i+1])
        total += sum(field[-i-1][N//2-i:N//2+i+1])
        i += 1

    print(f'#{t}', total)
