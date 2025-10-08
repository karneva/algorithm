# programmers 단어 변환

from collections import deque

def solution(begin, target, words):
    if target not in words:
        return 0

    word_len = len(begin)

    queue = deque([(begin, 0)])

    while queue:
        cur_w, cur_c = queue.popleft()

        for word in words:
            cnt = 0
            for i in range(word_len):
                if cur_w[i] == word[i]:
                    cnt += 1
            if cnt == word_len - 1:
                if word == target:
                    return cur_c + 1
                queue.append((word, cur_c+1))

if __name__ == "__main__":
    begin = 'hit'
    target = 'cog'
    words = ["hot", "dot", "dog", "lot", "log", "cog"]
    print(solution(begin, target, words))