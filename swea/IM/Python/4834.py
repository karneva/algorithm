# SWEA 4834 숫자 카드

for t in range(1, int(input())+1):
    N = int(input())
    num_list = list(map(int, input()))

    # 딕셔너리로 풀기
    num_dict = {}
    for num in num_list:
        # 처음 키가 입력되면 키 생성, 1 할당
        if num not in num_dict:
            num_dict.setdefault(num, 1)
        # 키가 이미 있으면 밸류에 1 추가
        else:
            num_dict[num] += 1
    # 밸류가 제일 큰 값의 키를 출력한다
    max_k = max(num_dict, key=lambda x:(num_dict[x], x))
    print(f'#{t}', max_k, num_dict[max_k])

# for t in range(1, int(input())+1):
#     N = int(input())
#     num_list = list(map(int, input()))

#     # 리스트로 풀기
#     cnt_list = [0] * (max(num_list)+1)
#     for num in num_list:
#         cnt_list[num] += 1

#     max_i = 0
#     for i in range(len(cnt_list)-1, -1, -1):
#         if i != 0 and cnt_list[i] == max(cnt_list):
#             if i > max_i:
#                 max_i = i
#                 break

#     print(f'#{t}', max_i, cnt_list[max_i])