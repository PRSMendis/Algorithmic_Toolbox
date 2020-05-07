# python3

from itertools import combinations


def compute_inversions_naive(a):
    number_of_inversions = 0
    for i, j in combinations(range(len(a)), 2):
        if a[i] > a[j]:
            number_of_inversions += 1
    return number_of_inversions


def compute_inversions(a):
    def merge_num_of_inv(b, c):
        d = list()
        num_of_inversions = 0
        while (len(b) != 0) and (len(c) != 0):
            if b[0] <= c[0]:
                d.append(b[0])
                b = b[1:]
            else:
                d.append(c[0])
                c = c[1:]
                num_of_inversions += len(b)
        d.extend(b)
        d.extend(c)
        return d, num_of_inversions



    # type here
    n = len(a)
    num_of_inversions = 0
    if n == 1:
        return a, num_of_inversions
    mid = n // 2
    b, n1 = compute_inversions(a[:mid])
    num_of_inversions += n1
    c, n2 = compute_inversions(a[mid:])
    num_of_inversions += n2
    a_new, n3 = merge_num_of_inv(b, c)
    num_of_inversions += n3
    return a_new, num_of_inversions



if __name__ == '__main__':
    # input_n = int(input())
    # elements = list(map(int, input().split()))
    # assert len(elements) == input_n
    # print(compute_inversions(elements))

    elements = [1, 2, 3]
    # elements = [3, 2, 1]
    print(compute_inversions(elements))

