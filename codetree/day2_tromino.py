# codetree 트로미노

n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

block = [
    [[1, 0],
    [1, 1]],
    [[1, 1],
    [1, 0]],
    [[0, 1],
    [1, 1]],
    [[1, 1],
    [0, 1]],
    [[1, 0, 0],
     [1, 0, 0],
     [1, 0, 0]],
    [[0, 1, 0],
     [0, 1, 0],
     [0, 1, 0]],
    [[0, 0, 1],
     [0, 0, 1],
     [0, 0, 1]],
    [[1, 1, 1],
     [0, 0, 0],
     [0, 0, 0]],
    [[0, 0, 0],
     [1, 1, 1],
     [0, 0, 0]],
    [[0, 0, 0],
     [0, 0, 0],
     [1, 1, 1]]
]

max_price = 0

for b in block:
    b_l = len(b)
    for i in range(n-b_l+1):
        for j in range(m-b_l+1):
            price = 0
            for k in range(b_l):
                price += sum([a*b for a, b in zip(grid[i+k][j:j+b_l], b[k])])
            if price > max_price:
                max_price = price
print(max_price)

'''
input
3 3
1 2 3
3 2 1
3 1 1
output
8

input
4 5
6 5 4 3 1
3 4 4 14 1
6 1 3 15 5
3 5 1 16 3
output
45
'''