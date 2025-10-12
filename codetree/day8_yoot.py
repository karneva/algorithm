# codetree 1차원 윳놀이

def solve():
    N, M, K = map(int, input().split())
    moves = list(map(int, input().split()))

    start = tuple([K] + [0] * (M - 1))

    states = {start}

    for t in range(N):
        d = moves[t]
        next_states = set()
        for hist in states:
            made = False
            for p_idx in range(M - 1):
                cnt_here = hist[p_idx]
                if cnt_here == 0:
                    continue
                pos = p_idx + 1
                new_pos = pos + d
                if new_pos > M:
                    new_pos = M
                np_idx = new_pos - 1

                new_hist = list(hist)
                new_hist[p_idx] -= 1
                new_hist[np_idx] += 1
                next_states.add(tuple(new_hist))
                made = True
            if not made:
                next_states.add(hist)

        states = next_states

    ans = max(h[M - 1] for h in states)
    print(ans)


if __name__ == "__main__":
    solve()

'''
input
4 6 3
2 4 2 4
output
2

input
6 10 3
5 3 2 2 3 3
output
2
'''