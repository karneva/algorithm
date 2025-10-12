# codetree XOR 결과 최대 만들기

n, m = tuple(map(int, input().split()))
a = list(map(int, input().split()))

ans = 0

def recursion(curr_idx, cnt, curr_xor):
    global ans

    if cnt >= m:
        ans = max(ans, curr_xor)
        return

    if curr_idx >= n or n - curr_idx < m - cnt:
        return

    recursion(curr_idx + 1, cnt, curr_xor)
    recursion(curr_idx + 1, cnt + 1, curr_xor ^ a[curr_idx])

recursion(0, 0, 0)
print(ans)

'''
input
5 3 
1 2 3 4 5
output
7
'''