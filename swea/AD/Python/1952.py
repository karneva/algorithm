# SWEA 1952 수영장

def plan(idx, price):
    global result
    # 백트래킹 조건
    if price >= result:
        return
    # 1년 다 됐으면 결과값 갱신
    if idx >= 12:
        result = min(result, price)
        return
    # 한달치는 일일권이랑 가격 비교해서 재귀 호출
    plan(idx+1, min(price+planner[idx]*D, price+M))
    plan(idx+3, price+Mmm)

T = int(input())

for t in range(1, T+1):
    D, M, Mmm, Y = map(int, input().split())
    planner = list(map(int, input().split()))

    result = 31 * 12 * 3000
    plan(0, 0)
    # 마지막으로 1년권이랑 비교
    result = min(Y, result)
    print(f'#{t}', result)
