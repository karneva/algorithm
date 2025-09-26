# SWEA GNS

T = int(input())

for t in range(1, T + 1):
    N, M = input().split()

    gns = ['ZRO', 'ONE', 'TWO', 'THR', 'FOR', 'FIV', 'SIX', 'SVN', 'EGT', 'NIN']

    numbers = list(input().split())

    cnt_list = [0] * 10

    # 해당 문자열의 인덱스를 찾아서 카운트 +1
    for num in numbers:
        cnt_list[gns.index(num)] += 1

    # 카운트 정렬 리스트에서 할당된 슷자 만큼 GNS 문자 반복 입력
    print(N, *[gns[idx] for idx, cnt in enumerate(cnt_list) for _ in range(cnt)])