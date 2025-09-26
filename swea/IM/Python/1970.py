# SWEA 1970 쉬운 거스름돈

T = int(input())
money = [50000, 10000, 5000, 1000, 500, 100, 50, 10]

for t in range(1, T+1):
    N = int(input())

    # 화폐 개수를 담을 리스트
    answer = []
    for i in money:
        # 몫과 나머지를 divmod로 동시에 계산
        div, mod = divmod(N, i)
        # 나머지는 다시 N에 할당, 몫은 결과 리스트에 추가
        N = mod
        answer.append(div)

    print(f'#{t}')
    print(*answer)