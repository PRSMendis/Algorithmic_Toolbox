# python3


def gcd_naive(a, b):
    assert 1 <= a <= 2 * 10 ** 9 and 1 <= b <= 2 * 10 ** 9

    for divisor in range(min(a, b), 0, -1):
        if a % divisor == 0 and b % divisor == 0:
            return divisor

    assert False


def gcd(a, b):
    # assert 0 <= a <= 2 * 10 ** 9 and 0 <= b <= 2 * 10 ** 9
    assert 1 <= a <= 2 * 10 ** 9 and 1 <= b <= 2 * 10 ** 9

    # type here
    # check = False
    numer = max(a,b)
    denom = min(a,b)
    rem = numer % denom
    # while check == False:
    while rem != 0:
        numer = denom
        denom = rem
        rem = numer % denom


    return denom



if __name__ == '__main__':
    input_a, input_b = map(int, input().split())
    print(gcd(input_a, input_b))
    # a,b = 0,12
    # print(gcd(a,b))
