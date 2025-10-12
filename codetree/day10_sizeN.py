# codetree 크기가 N인 순열

# next permutaion 방식
def next_perm(a):
    i = len(a) - 2
    while i >= 0 and a[i] >= a[i + 1]:
        i -= 1

    if i < 0:
        return False

    j = len(a) - 1
    while a[j] <= a[i]:
        j -= 1

    a[i], a[j] = a[j], a[i]
    a[i + 1:] = reversed(a[i + 1:])

    return True


n = int(input())
a = list(range(1, n + 1))
print(*a)
while next_perm(a):
    print(*a)

'''
input
3
output
1 2 3
1 3 2
2 1 3
2 3 1
3 1 2
3 2 1
'''