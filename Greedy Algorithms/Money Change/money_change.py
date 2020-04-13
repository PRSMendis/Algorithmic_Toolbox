# python3


def money_change(money):
    assert 0 <= money <= 10 ** 3
    # type here
    count = 0
    c1, c2 , c3 = 10 ,5 ,1
    while money != 0:
        if money // c1 > 0:
            count += money // c1
            money -= (c1 * (money // c1))

        elif money // c2 > 0:
            count += money // c2
            money -= (c2 * (money // c2))

        elif money // c3 > 0:
            count += money // c3
            money -= (c3 * (money // c3))

    return count



if __name__ == '__main__':
    input_money = int(input())
    print(money_change(input_money))
    # print(money_change(87))
    # print(80 // 7, 80 % 7)