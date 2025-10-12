# codetree N개 중에 M개 뽑기 dong 강사님 코드

N, M = map(int, input().split())
picked = []

# 1부터 n까지의 각 숫자(curr_num)을 조합에 포함할지 말지를 결정
# O(2^N)
def pick_one(curr_num):
    # 종료조건??
    if curr_num == N + 1:
        if len(picked) == M:
            print(*picked)
            return

# 현재 값을 뽑거나
    picked.append(curr_num)
    pick_one(curr_num + 1)
    picked.pop()

# 현재 값을 뽑지 않거나
    pick_one(curr_num + 1)

pick_one(1)

# ================================================

# 현재 idx-1까지 숫자를 뽑았고, idx번째 숫자를 뽑을 차례
# C(N, M)
def pick_two(idx):
# 종료조건??
    if idx == M:
        print(*picked)
        return
    
    if len(picked) > 0:
        for i in range(picked[-1] + 1, N + 1):
            picked.append(i)
            pick_two(idx + 1)
            picked.pop()
    else:
        for i in range(1, N + 1):
            picked.append(i)
            pick_two(idx + 1)
            picked.pop()

pick_two(0)

# ================================================

# 1부터 n까지의 각 숫자(curr_num)을 조합에 포함할지 말지를 결정
# C(N, M)
def pick_three(curr_num, count):
# 종료조건??
    if count == M:
        print(*picked)
        return
    if curr_num > N:
        return
    if count + (N - curr_num + 1) < M:
        return
    
    # 현재 값을 뽑거나
    picked.append(curr_num)
    pick_three(curr_num + 1, count + 1)
    picked.pop()
    
    # 현재 값을 뽑지 않거나
    pick_three(curr_num + 1, count)

pick_three(1, 0)

'''
input
3 2
output
1 2
1 3
2 3

input
4 3
output
1 2 3
1 2 4
1 3 4
2 3 4
'''