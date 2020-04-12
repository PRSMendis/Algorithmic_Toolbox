# python3


def fibonacci_number_naive(n):
    assert 0 <= n <= 45

    if n <= 1:
        return n

    # print("Computer F Sub", n)
    return fibonacci_number_naive(n - 1) + fibonacci_number_naive(n - 2)


def fibonacci_number(n):
    # assert 0 <= n <= 45

    # type here
    a = [0, 1, 1]
    if n > 2:
        for i in range(2, n):
            # print(a)
            a.append(a[i - 1] + a[i])
        return a[n]
        # return str(a[n])[-1]
        # if i == n:
        #     return a
    else:
        return a[n]
        # return str(a[n])


if __name__ == '__main__':
    input_n = int(input())
    # input_n = 10
    # n = 15
    # print(fibonacci_number_naive(n))
    # print(fibonacci_number(n))
    print(fibonacci_number(input_n))
