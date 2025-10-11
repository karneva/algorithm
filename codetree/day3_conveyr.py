# codetree 컨베이버 벨트

n, t = map(int, input().split())
u = list(map(int, input().split()))
d = list(map(int, input().split()))

new_list = u + d

for _ in range(t):
    tmp = new_list.pop()
    new_list = [tmp] + new_list

print(*new_list[:n])
print(*new_list[n:])

'''
input
3 1
1 2 3
6 5 1
output
1 1 2
3 6 5

input
3 3
1 2 3
6 5 1

output
6 5 1
1 2 3
'''