# programmers 2021 KAKAO 신규 아이디 추천

def step2(lst):
    allow = ['-', '_', '.']
    tmp = []
    for i in lst:
        if i.isalpha() or i.isdigit():
            tmp.append(i)
        else:
            if i in allow:
                tmp.append(i)
    return ''.join(tmp)

def step3(lst):
    while True:
        if '..' not in lst:
            return lst
        lst = lst.replace('..', '.')

def step4(lst):
    tmp = []
    for i in range(len(lst)):
        if i == 0 or i == len(lst)-1:
            if lst[i] != '.':
                tmp.append(lst[i])
        else:
            tmp.append(lst[i])
    return ''.join(tmp)

def step5(lst):
    if not lst:
        return 'a'
    else:
        return lst

def step6(lst):
    return step4(lst[:15])

def step7(lst):
    while len(lst) <= 2:
        lst += lst[-1]

    return lst

def solution(new_id):
    new_id = step2(new_id.lower())
    new_id = step3(new_id)
    new_id = step4(new_id)
    new_id = step5(new_id)
    new_id = step6(new_id)
    new_id = step7(new_id)

    return new_id

print(solution("...!@BaT#*..y.abcdefghijklm"))