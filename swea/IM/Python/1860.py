# SWEA 1860 진기의 최고급 붕어빵

T = int(input())

for t in range(1, T + 1):
    N, M, K = map(int, input().split())
    guest = list(map(int, input().split()))

    # 붕어빵을 굽는 시간은 손님 최대 시간이다
    bungeo = [0] * (max(guest)+1)
    # 시간 초마다 붕어빵 개수를 더해준다
    for i in range(M, len(bungeo), M):
        bungeo[i] += K

    total = 0
    for i in range(max(guest) + 1):
        total += bungeo[i]
        # 손님이 온 시간이면 현재 붕어빵에서 -1
        if i in guest:
            total -= 1
        # 붕어빵 개수가 0 밑이면 실패!
        if total < 0:
            print(f"#{t} Impossible")
            break
    else:
        print(f"#{t} Possible")