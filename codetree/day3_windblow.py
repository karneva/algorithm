# codetree 1차원 바람

from collections import deque

n, m, q = map(int, input().split())
a = [deque(map(int, input().split())) for _ in range(n)]
winds = [(int(r), d) for r, d in [input().split() for _ in range(q)]]

def blow_wind(arr, dir):
    if dir == 'L':
        tmp = arr.pop()
        arr.appendleft(tmp)
    else:
        tmp = arr.popleft()
        arr.append(tmp)
    return

def wave_up_wind(idx, d):
    up_idx = idx - 1
    if up_idx < 0:
        return
    nd = 'L' if d == 'R' else 'R'
    if any(a[up_idx][i] == a[idx][i] for i in range(m)):
        blow_wind(a[up_idx], nd)
        wave_up_wind(up_idx, nd)

def wave_down_wind(idx, d):
    down_idx = idx + 1
    if down_idx >= n:
        return
    nd = 'L' if d == 'R' else 'R'
    if any(a[down_idx][i] == a[idx][i] for i in range(m)):
        blow_wind(a[down_idx], nd)
        wave_down_wind(down_idx, nd)

for row, dir in winds:
    idx = row - 1
    blow_wind(a[idx], dir)

    wave_up_wind(idx, dir)
    wave_down_wind(idx, dir)

for i in a:
    print(*i)


'''
input
6 5 1
1 5 6 7 3
5 3 2 5 4
6 4 5 2 5
2 6 1 0 5
5 1 2 1 6
4 2 5 2 8
3 L
output
1 5 6 7 3
3 2 5 4 5
5 6 4 5 2
6 1 0 5 2
6 5 1 2 1
2 5 2 8 4

input
3 3 2
1 2 3
3 2 1
3 3 3
3 L
1 L
output
2 3 1
1 3 2
3 3 3
'''