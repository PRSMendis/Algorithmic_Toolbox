# python3
from functools import lru_cache

def last_digit_of_fibonacci_number_naive(n):
    assert 0 <= n <= 10 ** 7

    if n <= 1:
        return n

    return (last_digit_of_fibonacci_number_naive(n - 1) + last_digit_of_fibonacci_number_naive(n - 2)) % 10


def last_digit_of_fibonacci_number(n):
    assert 0 <= n <= 10 ** 7

    # type here
    def fibo(n):
        a, b = 0, 1
        for i in range(n):
            a, b = b, (a + b) % 10
        return a

    # def fibo(n, stored = { 0:0 , 1:1}):
    #     if n not in stored:
    #         stored[n] = fibo(n-1, stored) + fibo(n-2, stored)
    #     return stored[n]


    # @lru_cache(1000)
    # def fibo(n):
    #     if n == 0:
    #         return 0
    #     elif n == 1 or n ==2:
    #         return 1
    #     else:
    #         return fibo(n-1) + fibo(n-2)
    # return int(str(fibo(n))[-1])
    return int(str(fibo(n))[-1])
#



if __name__ == '__main__':
    input_n = int(input())
    print(last_digit_of_fibonacci_number(input_n))
    # for i in range(0,100):
    #     print(last_digit_of_fibonacci_number(i))
