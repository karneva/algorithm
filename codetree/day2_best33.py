# codetree 최고의 33위치

n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

max_price = 0
for i in range(n-3+1):
    for j in range(n-3+1):
        price = 0
        for k in range(3):
            price += sum([1 for x in grid[i+k][j:j+3] if x == 1])
        if price > max_price:
            max_price = price

print(max_price)

'''
input
3
1 0 1
0 1 0
0 1 0
output
4
input
5
0 0 0 1 1
1 0 1 1 1
0 1 0 1 0
0 1 0 1 0
0 0 0 1 1
output
6
'''