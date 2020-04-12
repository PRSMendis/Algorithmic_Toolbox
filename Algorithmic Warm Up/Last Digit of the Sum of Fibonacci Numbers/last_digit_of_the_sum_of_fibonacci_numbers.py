# python3


def last_digit_of_the_sum_of_fibonacci_numbers_naive(n):
    assert 0 <= n <= 10 ** 18

    if n <= 1:
        return n

    fibonacci_numbers = [0] * (n + 1)
    fibonacci_numbers[0] = 0
    fibonacci_numbers[1] = 1
    for i in range(2, n + 1):
        fibonacci_numbers[i] = fibonacci_numbers[i - 2] + fibonacci_numbers[i - 1]

    return sum(fibonacci_numbers) % 10


def last_digit_of_the_sum_of_fibonacci_numbers(n):
    assert 0 <= n <= 10 ** 18
    #options - use golden ratio, tallying sum, regular fibonacci



    #type here
    fibcache = {}
    def fibo(n):
        if n in fibcache:
            return fibcache[n]

        if n == 0 :
            val  = 0
        elif n == 1 or n == 2:
            val = 1
        else:
            val = fibo(n-1) + fibo(n-2)

        fibcache[n] = val
        return val

    return int(str(fibo(n+2) - 1)[-1])




if __name__ == '__main__':
    input_n = int(input())
    print(last_digit_of_the_sum_of_fibonacci_numbers(input_n))
    # for n in range (0,5):
    #     print(last_digit_of_the_sum_of_fibonacci_numbers(n))