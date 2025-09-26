# SWEA 1206 VIEW

for t in range(1, 11):
    N = int(input())
    buildings = list(map(int, input().split()))

    # 왼쪽 두칸부터 오른쪽 두칸까지 델타
    delta = [-2, -1, 1, 2]
    river_view = 0
    for b in range(2, N-2):
        # 건물의 높이는 255까지니까
        cnt = 255
        for d in delta:
            view = b + d
            # 한번이라도 조망권이 보장되지 않으면 break
            if buildings[b] <= buildings[view]:
                break
            # 조망권이 보장되면 가장 차이가 적은 값 계산
            else:
                if cnt > buildings[b] - buildings[view]:
                    cnt = buildings[b] - buildings[view]
        # 조망권이 보장되면 보장되는 세대 수만 추가
        else:
            river_view += cnt

    print(f'#{t}', river_view)