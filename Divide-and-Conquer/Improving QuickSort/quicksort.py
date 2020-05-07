# python3

# from random import randint, random

import random

def partition3(a, left, right):
    # type here
    p_val = a[left]
    p_l = i = left
    p_e = right
    while i <= p_e:
        if a[i] < p_val:
            a[i], a[p_l] = a[p_l], a[i]
            p_l += 1
            i += 1
        elif a[i] == p_val:
            i += 1
        else:
            a[i], a[p_e] = a[p_e], a[i]
            p_e -= 1
        pIndexes = [p_l, p_e]
    return pIndexes


def randomized_quick_sort(a, left, right):
    if left >= right:
        return
#     make a call to partition3 and then two recursive calls
# to randomized_quick_sort
    k = random.randint(left, right)
    a[left], a[k] = a[k], a[left]
    pIndex = partition3(a, left, right)
    randomized_quick_sort(a, left, pIndex[0] - 1)
    randomized_quick_sort(a, pIndex[1] + 1, right)


if __name__ == '__main__':
    input_n = int(input())
    elements = list(map(int, input().split()))
    assert len(elements) == input_n


    # elements = [1, 2, 3, 5, 6, 6, 7, 8]

    randomized_quick_sort(elements, 0, len(elements) - 1)
    print(*elements)
