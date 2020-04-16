# python3

from sys import stdin
from pandas import DataFrame

def maximum_loot_value(capacity, weights, prices):
    assert 0 <= capacity <= 2 * 10 ** 6
    assert len(weights) == len(prices)
    assert 1 <= len(weights) <= 10 ** 3
    assert all(0 < w <= 2 * 10 ** 6 for w in weights)
    assert all(0 <= p <= 2 * 10 ** 6 for p in prices)

    print(capacity)
    value = 0

    inv = {'Weight': weights,
           'Price': prices,
           'P/W': [int(a / b) for a, b in zip(prices, weights)]
           }

    df = DataFrame(inv, columns=['Weight', 'Price', 'P/W'])

    df = df.sort_values(by='P/W', ascending=False)

    A = df.to_numpy()
    #     print(A)

    #     print(capacity)
    for x in range(0, len(A)):
        #         print(A[x])
        #         print(A[x][)
        # 0 = weight
        # 1 = Price
        # 2 = P/W
        if capacity == 0:
            # break
            return value
        elif capacity >= A[x][0]:
            value += A[x][1]
            capacity -= A[x][0]
        #             print(value, capacity, A[x][0])
        elif capacity < A[x][0]:
            #             print(value, capacity, A[x][0])
            #             print(A[x][1] / (A[x][0]/capacity))
            # take as much as you can
            value += (A[x][1] / (A[x][0] / capacity))
            capacity -= capacity
    return value


if __name__ == "__main__":
    # data = list(map(int, stdin.read().split()))
    # n, input_capacity = data[0:2]
    # input_prices = data[2:(2 * n + 2):2]
    # input_weights = data[3:(2 * n + 2):2]
    capacity, weights, prices = 50, [20, 50, 30], [60, 100, 120]

    # opt_value = maximum_loot_value(input_capacity, input_weights, input_prices)
    opt_value = maximum_loot_value(capacity, weights, prices)
    print("{:.10f}".format(opt_value))
