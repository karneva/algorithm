# codetree 아름다운 수

def count_beautiful(n):
    ans = 0

    def dfs(pos, last, run_len):
        nonlocal ans
        if pos == n:
            # 마지막 run도 배수여야 유효
            if run_len % last == 0:
                ans += 1
            return

        for v in (1, 2, 3, 4):
            if last == 0:
                # 시작: 어떤 값이든 가능, run_len=1로 시작
                dfs(pos + 1, v, 1)
            elif v == last:
                # 같은 값은 자유롭게 이어붙이기
                dfs(pos + 1, last, run_len + 1)
            else:
                # 다른 값으로 바꿀 수 있는 건 '직전 run이 완료(배수)'인 경우뿐
                if run_len % last == 0:
                    dfs(pos + 1, v, 1)

    dfs(0, 0, 0)
    return ans

if __name__ == "__main__":
    n = int(input().strip())
    print(count_beautiful(n))

'''
input
1
output
1

input
3
출력
output
4
'''