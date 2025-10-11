# codetree 삼각형 컨베이어 벨트

n, t = map(int, input().split())

l = list(map(int, input().split()))
r = list(map(int, input().split()))
d = list(map(int, input().split()))

new_list = l + r + d

for _ in range(t):
    tmp = new_list.pop()
    new_list = [tmp] + new_list

print(*new_list[:n])
print(*new_list[n:2*n])
print(*new_list[2*n:])

'''
input
3 1
1 2 4
5 9 3
6 5 1
output
1 1 2
4 5 9
3 6 5

input
3 3
1 2 4
5 9 3
6 5 1
output
6 5 1
1 2 4
5 9 3
'''