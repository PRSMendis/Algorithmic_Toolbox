# python3


def lcm_naive(a, b):
    assert 1 <= a <= 2 * 10 ** 9 and 1 <= b <= 2 * 10 ** 9

    multiple = max(a, b)
    while multiple % a != 0 or multiple % b != 0:
        multiple += 1

    return multiple


def lcm(a, b):
    assert 1 <= a <= 2 * 10 ** 9 and 1 <= b <= 2 * 10 ** 9

    # type here
#     Can find LCM by first finding greatest common multiple
    numer = max(a,b)
    denom = min(a,b)
    rem = numer % denom
    # while check == False:
    while rem != 0:
        numer = denom
        denom = rem
        rem = numer % denom


    return int((a*b) / denom)


if __name__ == '__main__':
    input_a, input_b = map(int, input().split())
    print(lcm(input_a, input_b))
    # a,b = 3, 2
    # print(lcm(a,b))
