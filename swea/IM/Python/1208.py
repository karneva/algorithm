# Flatten

for t in range(1, 11):
    N = int(input())
    arr = list(map(int, input().split()))

    # 큰 수에서 1 빼기, 작은 수에서 1 빼기를 N번 반복
    for _ in range(N):
        arr[arr.index(max(arr))] -= 1
        arr[arr.index(min(arr))] += 1

    print(f'#{t}', max(arr) - min(arr))