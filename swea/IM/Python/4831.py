# SWEA 4831 전기버스

T = int(input())
 
for t in range(1, T+1):
    K, N, M = map(int, input().split())
    arr = list(map(int, input().split()))
 
    station = [0] * (N+1)
 
    for i in range(len(arr)):
        station[arr[i]] += 1
 
    cnt = 0
    i = 0
 
    while i < len(station):
        imsi = station[i+1:i+K+1]
        if 1 not in imsi:
            cnt = 0
            break
        else:
            for j in range(len(imsi) - 1, -1, -1):
                if imsi[j] == 1:
                    cnt += 1
                    i += (j + 1)
                    break
 
        if i + K >= len(station) - 1:
            break
 
    print(f'#{t} {cnt}')