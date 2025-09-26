# SWEA 4835 구간합

for t in range(1, int(input())+1):
    N, M = map(int, input().split())
    num_list = list(map(int, input().split()))

    max_sum = 0
    min_sum = 50000000
    for num in range(N-M+1):
        sum_ = sum(num_list[num:num+M])
        if sum_ > max_sum:
            max_sum = sum_
            continue
        if sum_ < min_sum:
            min_sum = sum_

    print(f'#{t}', max_sum-min_sum)