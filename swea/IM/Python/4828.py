# SWEA 4828 min max

for t in range(1, int(input())+1):
    N = int(input())
    num_list = list(map(int, input().split()))
    print(f'#{t}', max(num_list)-min(num_list))