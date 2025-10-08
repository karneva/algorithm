# programmers 2020 KAKAO 문자열 압축

def solution(s):
    word_len = len(s)
    result = word_len
    cut = 1
    i = 0
    cnt = 1
    answer = []
    while cut < word_len:
        if i >= word_len:
            result = min(result, len(answer))
            answer.clear()
            cut += 1
            i = 0

        nxt_idx = i+cut

        if s[i:i+cut] != s[nxt_idx:nxt_idx+cut]:
            if cnt > 1:
                answer.extend(list(str(cnt)))
            answer.extend(s[i:i+cut])
            cnt = 1
        else:
            cnt += 1
        i = nxt_idx

    return result

if __name__ == "__main__":
    for _ in range(5):
        s = input()
        print(solution(s))