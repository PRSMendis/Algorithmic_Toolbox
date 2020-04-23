# python3


def compute_min_number_of_refills(d, m, stops):
    assert 1 <= d <= 10 ** 5
    assert 1 <= m <= 400
    assert 1 <= len(stops) <= 300
    assert 0 < stops[0] and all(stops[i] < stops[i + 1] for i in range(len(stops) - 1)) and stops[-1] < d

    # type here
    # print("hello")
    # print(d,m, stops)
    start = 0
    position = 0
    fuel = m
    refills = 0
    stops.append(d)
    i = 0

    # While we have not reached the destination
    while position != d:
        # Find the greatest distance that we can travel, and go there and refill our fuel
        greatest_pos = position
        while i < len(stops):

            if greatest_pos == d:
                refills +=1
                position = greatest_pos
                break

            elif fuel + position >= stops[i]:
                if stops[i] > greatest_pos:
                    greatest_pos = stops[i]
                    # print(greatest_pos)
                    if greatest_pos == d:
                        position = greatest_pos
                        break


            elif fuel + position < stops[i]:
                refills += 1
                position = greatest_pos
                break
            i +=1



            # elif greatest_pos == d:
            #     refills +=1
            #     position = greatest_pos
            #     break
    return refills



            # else:








if __name__ == '__main__':
    input_d = int(input())
    input_m = int(input())
    input_n = int(input())
    input_stops = list(map(int, input().split()))
    assert len(input_stops) == input_n

    print(compute_min_number_of_refills(input_d, input_m, input_stops))
    # (d, m, stops ) = (950, 400, [200, 375, 550, 750])
    print(compute_min_number_of_refills(d, m, stops))