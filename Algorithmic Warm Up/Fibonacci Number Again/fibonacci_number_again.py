# python3


def fibonacci_number_again_naive(n, m):
    assert 0 <= n <= 10 ** 18 and 2 <= m <= 10 ** 3

    if n <= 1:
        return n

    previous, current = 0, 1
    for _ in range(n - 1):
        previous, current = current, (previous + current) % m

    return current


def fibonacci_number_again(n, m):
    assert 0 <= n <= 10 ** 18 and 2 <= m <= 10 ** 3

    #type here
    a = [0, 1, 1]
    modu = [0,1,1]
    check = False
    # print(modu)
    if n > 2:
    # if m > 2:
    #     while check == False:
        for i in range(2, n):
            if check == True:
                break

        # for i in range(2, min(m,1000)):
            # print(a)
            f = a[i - 1] + a[i]
            a.append(f)

            # Check if sequence is repeated yet

            if i!= 2 and modu[i] == modu[i-1] == 1 and modu[i-2] == 0:
                check = True
            else:
                modf = f % m
                # print(modf)
                modu.append(modf)

        # del modu[i - 2:i + 1]
        del modu[i - 3:i]
        period = len(modu)
    # print(n,period, n%period)

        return modu[n%period]

        # return a[n]
        # return modu
        # return str(a[n])[-1]
        # if i == n:
        #     return a
    else:
        return a[n]
        # return str(a[n])


if __name__ == '__main__':
    # input_n, input_m = map(int, input().split())
    # print(fibonacci_number_again(input_n, input_m))
    n,m = 2015, 4
    print(fibonacci_number_again(n,m))
