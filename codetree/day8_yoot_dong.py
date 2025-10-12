# codetree 1차원 윳놀이 dong 강사님 코드

# n: 턴의 수, m: 끝점의 좌표, k: 말의 수, nums: 턴마다 움직일 거리
n, m, k = map(int, input().split())
movings = list(map(int, input().split()))

positions = [1] * (k + 1)
ans = 0

def calc():
    # m에 도달한 말이 몇개인지 센다.
    cnt = 0
    for i in range(1, k + 1):
        if positions[i] >= m:
            cnt += 1
            return cnt

# idx는 moving의 index = 현재 몇 번쨰 움직임을 진행할지
def move(idx):
    global ans

    if idx == n:
        # print(movings)
        ans = max(ans, calc())
        return

    for i in range(1, k + 1):
        if k > 1 and positions[i] >= m:
            continue

        positions[i] += movings[idx] # i를 움직인다.
        move(idx + 1) # 재귀를 한다.
        positions[i] -= movings[idx] # i의 움직임을 돌려놓는다.

move(0)
print(ans)

'''
input
4 6 3
2 4 2 4
output
2

input
6 10 3
5 3 2 2 3 3
output
2
'''