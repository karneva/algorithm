# SWEA 1211 ladder2

for t in range(1, 11):
    N = int(input())
    ladder = [list(map(int, input().split())) for _ in range(100)]

    start_point = []
    # 출발 지점 인덱스 기록
    for i in range(100):
        if ladder[0][i] == 1:
            start_point.append(i)

    # 방향은 아래, 좌우
    di = [1, 0, 0]
    dj = [0, 1, -1]

    # 초기 방향은 아래
    vec = 0
    min_cnt = 10000000
    min_sp = 0
    for sp in start_point:
        load_i, load_j = 0, sp
        cnt = 0
        while load_i < 100:
            # 아래로 가는 중일 때
            if vec == 0:
                # 좌우에 1이 있는지 없는지 검사
                for i in range(1, 3):
                    # 1이 있으면 그 쪽으로 방향 틀기
                    if (0 <= load_j + dj[i] < 100) and ladder[load_i + di[i]][load_j + dj[i]] == 1:
                        vec = i
                        break
            # 좌우로 가는 중일때
            else:
                # 아래쪽에 1이 있다면 위로 방향 틀기
                if ladder[load_i + di[0]][load_j + dj[0]] == 1:
                    vec = 0

            # 다음 좌표에 맞게 좌표 설정
            load_i += di[vec]
            load_j += dj[vec]
            cnt += 1

        if cnt <= min_cnt:
            min_cnt = cnt
            min_sp = sp

    print(f'#{N} {min_sp}')