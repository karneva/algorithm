import sys
sys.stdin = open('input.txt')

def recur(n, path):
    global cnt
    if len(path) == n:
        if is_pretty(path):
            cnt += 1
        return

    for i in range(1, 5):
        path.append(i)
        recur(n, path)
        path.pop()

def is_pretty(path):
    curr_idx = 0
    for i in range(1, n):
        if path[curr_idx] == path[i]:
            continue
        else:
            cnt = i - curr_idx
            if cnt % path[curr_idx] != 0:
                return False
            curr_idx = i

    cnt = n - curr_idx

    if cnt % path[curr_idx] != 0:
        return False

    return True

if __name__ == "__main__":
    n = int(input())
    path = []
    cnt = 0
    recur(n, path)
    print(cnt)