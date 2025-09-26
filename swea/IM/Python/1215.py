# SWEA 1215 회문1

for t in range(1, 11):
    N = int(input())
    arr = [list(input()) for _ in range(8)]

    cnt = 0
    # 가로로 회문 검사는 슬라이싱을 써서 검사
    for i in range(8):
        for j in range(8-N+1):
            if arr[i][j:j+N][::-1] == arr[i][j:j+N]:
                cnt += 1

    # 세로로 회문 검사는 양 끝에서부터 같은 위치가 같은지 검사
    for i in range(8-N+1):
        for j in range(8):
            for k in range(N//2):
                if arr[i+k][j] != arr[i+N-k-1][j]:
                    break
            else:
                cnt += 1

    print(f'#{t}', cnt)