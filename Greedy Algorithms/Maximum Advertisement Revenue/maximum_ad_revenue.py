# python3

from itertools import permutations
from itertools import product
from functools import reduce
import operator


def max_dot_product_naive(first_sequence, second_sequence):
    assert len(first_sequence) == len(second_sequence)
    assert len(first_sequence) <= 10 ** 3
    assert all(0 <= f <= 10 ** 5 for f in first_sequence)
    assert all(0 <= s <= 10 ** 5 for s in second_sequence)

    max_product = 0
    for permutation in permutations(second_sequence):
        dot_product = sum(first_sequence[i] * permutation[i] for i in range(len(first_sequence)))
        max_product = max(max_product, dot_product)

    return max_product


def max_dot_product(first_sequence, second_sequence):
    assert len(first_sequence) == len(second_sequence)
    assert len(first_sequence) <= 10 ** 3
    assert all(0 <= f <= 10 ** 5 for f in first_sequence)
    assert all(0 <= s <= 10 ** 5 for s in second_sequence)

    def prod(iterable):
        return reduce(operator.mul, iterable, 1)

    first_sequence.sort(reverse = True)
    second_sequence.sort(reverse = True)
    # print(first_sequence, second_sequence)
    a = list(zip(first_sequence, second_sequence))
    sum = 0
    for n in a:
        # print(n)
        # print(prod(n))
        sum += prod(n)
    # print(a)
    return sum




    # return ""


if __name__ == '__main__':
    n = int(input())
    prices = list(map(int, input().split()))
    clicks = list(map(int, input().split()))
    assert len(prices) == len(clicks) == n

    # prices, clicks = [2,3,5], [10,20,30]
    print(max_dot_product(prices, clicks))
    # print(prices)