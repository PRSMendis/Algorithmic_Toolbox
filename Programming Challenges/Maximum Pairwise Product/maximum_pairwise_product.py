# python3


def max_pairwise_product_naive(numbers):
    assert len(numbers) >= 2
    assert all(0 <= x <= 2 * 10 ** 5 for x in numbers)

    product = 0

    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            product = max(product, numbers[i] * numbers[j])

    return product


def max_pairwise_product(numbers):
    assert len(numbers) >= 2
    assert all(0 <= x <= 2 * 10 ** 5 for x in numbers)
    m1 = 0
    m2 = 0
    for num in numbers:
        # print(num)
        if num > m2:
            # print("r1:" + str(num))
            if num > m1:
                m2 = m1
                m1 = num
                # print(m1, m2)
            else:
                m2 = num
    return m1 * m2

    # type here




if __name__ == '__main__':
    n = int(input())
    input_numbers = list(map(int, input().split()))
    assert len(input_numbers) == n
    print(max_pairwise_product(input_numbers))
    # n = 10
    # A = [0] * n
    # print(max_pairwise_product_naive(A))
    # print("not good")
