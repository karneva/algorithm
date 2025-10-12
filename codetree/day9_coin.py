# codetree 단순한 동전 챙기기

from itertools import combinations

def solve():
    n = int(input().strip())
    grid = []
    for _ in range(n):
        line = input().strip()
        toks = line.split()
        if len(toks) == n:
            grid.append(toks)
        else:
            grid.append(list(line))

    S = E = None
    coins_by_val = [[] for _ in range(10)]  # 1..9 사용

    for i in range(n):
        for j in range(n):
            ch = grid[i][j]
            if ch == 'S':
                S = (i, j)
            elif ch == 'E':
                E = (i, j)
            elif ch.isdigit():
                v = int(ch)
                if 1 <= v <= 9:
                    coins_by_val[v].append((i, j))

    if S is None or E is None:
        print(-1)
        return

    # 사용 가능한 값 목록(오름차순)
    vals = [v for v in range(1, 10) if coins_by_val[v]]
    if len(vals) < 3:
        print(-1)
        return

    def dist(a, b):
        return abs(a[0]-b[0]) + abs(a[1]-b[1])

    INF = 10**18
    ans = INF

    # 길이 3..len(vals) 의 값 부분수열을 모두 시도
    for L in range(3, len(vals)+1):
        for seq in combinations(vals, L):
            # v1 그룹: S에서 각 동전까지
            prev_costs = [dist(S, p) for p in coins_by_val[seq[0]]]
            if not prev_costs:  # 방어
                continue

            # v2..vL 그룹 DP
            for idx in range(1, L):
                cur_group = coins_by_val[seq[idx]]
                if not cur_group:
                    prev_costs = None
                    break

                new_costs = [INF] * len(cur_group)
                # 각 q \in cur_group에 대해 min_p (prev_cost + dist(p,q))
                for qi, q in enumerate(cur_group):
                    best = INF
                    for pi, p in enumerate(coins_by_val[seq[idx-1]]):
                        cand = prev_costs[pi] + dist(p, q)
                        if cand < best:
                            best = cand
                    new_costs[qi] = best

                prev_costs = new_costs

            if prev_costs is None:
                continue

            # 마지막 그룹에서 E까지
            last_group = coins_by_val[seq[-1]]
            for li, r in enumerate(last_group):
                cand = prev_costs[li] + dist(r, E)
                if cand < ans:
                    ans = cand

    print(ans if ans < INF else -1)

if __name__ == "__main__":
    solve()

'''
input
4
..3.
2..E
.1..
5S.4
output
8

input
4
..3.
...E
.1..
.S..
output
-1
'''