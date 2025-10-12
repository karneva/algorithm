# codetree 특정 조건에 맞게 K개 중에 1개를 N번 뽑기 dong 강사님 코드

K, N = map(int, input().split())

picked = []

def pick(cnt):
    # 종료조건
    if cnt == N:
        print(*picked)
        return

    for i in range(1, K + 1):
        if (len(picked) >= 2 and picked[-2] == picked[-1] and i == picked[-1]):
            continue
    
        picked.append(i)
        pick(cnt + 1)
        picked.pop()

pick(0)

'''
input
2 1
output
1
2

input
2 3
output
1 1 2
1 2 1
1 2 2
2 1 1
2 1 2
2 2 1
'''