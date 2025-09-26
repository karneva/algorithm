# SWEA 1210 ladder1

for t in range(1, 11):
    N = int(input())
    ladder = [list(map(int, input().split())) for _ in range(100)]

    arrive_j = 0

    # 밑에서부터 올라갈거니까 2 찾기
    for i in range(len(ladder[99])):
        if ladder[99][i] == 2:
            arrive_j = i

    # 방향은 위, 좌우
    di = [-1, 0, 0]
    dj = [0, 1, -1]

    load_i, load_j = 98, arrive_j
    # 초기 방향은 위
    vec = 0
    while load_i > 0:
        # 위로 가는 중일 때
        if vec == 0:
            # 좌우에 1이 있는지 없는지 검사
            for i in range(1, 3):
                # 1이 있으면 그 쪽으로 방향 틀기
                if (0 <= load_j + dj[i] < 100) and ladder[load_i + di[i]][load_j + dj[i]] == 1:
                    vec = i
        # 좌우로 가는 중일때
        else:
            # 위쪽에 1이 있다면 위로 방향 틀기
            if ladder[load_i + di[0]][load_j + dj[0]] == 1:
                vec = 0
        
        # 다음 좌표에 맞게 좌표 설정
        load_i += di[vec]
        load_j += dj[vec]

    print(f'#{N} {load_j}')