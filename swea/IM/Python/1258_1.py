# SWEA 1288 행렬찾기

def is_bomb(i, j):
    di, dj = 1, 1

    # 0 발견하기 전까지 범위 늘리기, N 벗어나면 자동으로 break
    while warehouse[i][j+dj] != 0:
        dj += 1
        if j + dj == N:
            break
    while warehouse[i+di][j] != 0:
        di += 1
        if i + di == N:
            break
    
    # 해당 범위만큼 원래 리스트 0으로 만들어버리기
    for ni in range(i, i+di):
        for nj in range(j, j+dj):
            warehouse[ni][nj] = 0

    return di, dj

for t in range(1, int(input())+1):
    N = int(input())
    warehouse = [list(map(int, input().split())) for _ in range(N)]

    bomb = []

    # 순회하면서 0이 아닌 숫자를 발견하면 그 좌표를 중심으로 범위 탐색
    for i in range(N):
        for j in range(N):
            if warehouse[i][j] != 0:
                x, y = is_bomb(i, j)
                bomb.append([x, y])
    # 행렬 크기 순으로 오름차순, 값이 같으면 행 크기로 오름차순
    bomb.sort(key=lambda x:(x[0] * x[1], x[0]))

    # T, 행렬 개수, 행 열 출력
    print(f'#{t} {len(bomb)}', end=' ')
    for i in bomb:
        print(*i, end=' ')
    print()