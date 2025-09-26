# SWEA 1959 두 개의 숫자열

T = int(input())
 
for t in range(1, T+1):
    N, M = map(int, input().split())
 
    # arr1에 길이가 더 긴 리스트를 할당
    if N >= M:
        arr1 = list(map(int, input().split()))
        arr2 = list(map(int, input().split()))
    else:
        arr2 = list(map(int, input().split()))
        arr1 = list(map(int, input().split()))
 
    # 최댓값 비교할 변수
    max_sum = 0
 
    # 전체적으로 abs(N-M)+1 번 밖에 돌 수 없다.
    for i in range(abs(N-M)+1):
        total = 0
        for x, y in zip(arr1[i:i+M], arr2):
            total += x * y
 
        if total > max_sum:
            max_sum = total
 
    print(f'#{t} {max_sum}')
