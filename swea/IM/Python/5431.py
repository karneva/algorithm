# SWEA 5431 민석이의 과제 체크하기

for t in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    print(f'#{t}', *[i for i in range(1, N+1) if i not in arr])