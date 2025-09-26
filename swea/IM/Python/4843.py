# SWEA 4843 특별한 정렬

for t in range(1, int(input()) + 1):
    N = int(input())
    arr = list(map(int, input().split()))

    for i in range(10):
        if i % 2 == 0:
            max_i = N-1
            for j in range(i, N):
                if arr[j] > arr[max_i]:
                    max_i = j
            arr[max_i], arr[i] = arr[i], arr[max_i]
        else:
            min_i = 0
            for j in range(i, N):
                if arr[j] < arr[min_i]:
                    min_i = j
            arr[min_i], arr[i] = arr[i], arr[min_i]

    print(f'#{t}', *arr[:10])