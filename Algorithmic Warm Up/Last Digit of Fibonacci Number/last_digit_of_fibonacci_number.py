# python3


def last_digit_of_fibonacci_number_naive(n):
    assert 0 <= n <= 10 ** 7

    if n <= 1:
        return n

    return (last_digit_of_fibonacci_number_naive(n - 1) + last_digit_of_fibonacci_number_naive(n - 2)) % 10


def last_digit_of_fibonacci_number(n):
    assert 0 <= n <= 10 ** 7

    # type here
    a = 0
    b = 1
    if n == 0:
        return a
    elif n == 1:
        return b
    else:
        for i in range(1,n):
            c = a + b
            a = b
            b = c
        # return b
        return int(str(b)[-1])



    # a = [0, 1, 1]
    # if n > 2:
    #     for i in range(2, n):
    #         # print(a)
    #         a.append(a[i - 1] + a[i])
    #         # del a[0]
    #         # if n > 5:
    #         #     del a[0]
    #     # return a
    #     return int(str(a[n]))
    #     # return int(str(a[n])[-1])
    #     # if i == n:
    #     #     return a
    # else:
    #     return a[n]
    #     # return str(a[n])


if __name__ == '__main__':
    input_n = int(input())
    print(last_digit_of_fibonacci_number(input_n))
    # for i in range(0,100):
    #     print(last_digit_of_fibonacci_number(i))
