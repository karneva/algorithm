# SWEA 4466 최대 성적표 만들기

for t in range(1, int(input()) + 1):
    N, K = map(int, input().split())
    field = list(map(int, input().split()))
    print(f'#{t}', sum(sorted(field, reverse=True)[:K]))