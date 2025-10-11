# codetree 1차원 젠가

n = int(input())
blocks = [int(input()) for _ in range(n)]
s1, e1 = map(int, input().split())
s2, e2 = map(int, input().split())

b1 = blocks[:s1-1] + blocks[e1:]
b2 = b1[:s2-1] + b1[e2:]
print(len(b2))
for i in b2:
    print(i)


'''
input
6
1
2
3
1
1
5
2 4
2 2
output
2
1
5

input
6
1
2
3
1
1
5
2 4
1 3
output
0
'''