# programmers 피로도

def solution(k, dungeons):
    def recur(df, cnt):
        nonlocal result

        result = max(result, cnt)

        for idx in range(len(dungeons)):
            if cleared[idx]:
                continue
            if df >= dungeons[idx][0]:
                cleared[idx] = True
                recur(df-dungeons[idx][1], cnt+1)
                cleared[idx] = False

    result = 0
    cleared = [False] * len(dungeons)
    recur(k, 0)

    return result

if __name__ == "__main__":
    print(solution(80, [[80,20],[50,40],[30,10]]))