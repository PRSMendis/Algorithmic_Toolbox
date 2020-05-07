# python3


def majority_element_naive(elements):
    assert len(elements) <= 10 ** 5
    for e in elements:
        if elements.count(e) > len(elements) / 2:
            return 1

    return 0


def majority_element(elements, left, right):
    assert len(elements) <= 10 ** 5
    # type here

    if left == right:
        return -1
    if left + 1 == right:
        return elements[left]

    l_ele = majority_element(elements, left, (left + right - 1) // 2 + 1)
    r_ele = majority_element(elements, (left + right - 1) // 2 + 1, right)

    lcount = 0
    for i in range(left, right):
        if elements[i] == l_ele:
            lcount += 1
    if lcount > (right - left) // 2:
        return l_ele

    rcount = 0
    for i in range(left, right):
        if elements[i] == r_ele:
            rcount += 1
    if rcount > (right - left) // 2:
        return r_ele

    return -1


if __name__ == '__main__':
    # input_n = int(input())
    # input_elements = list(map(int, input().split()))
    # assert len(input_elements) == input_n
    # print(majority_element(input_elements,0,len(input_elements)))

    # input_elements = [7, 2, 7,2]
    input_elements = [2, 3, 9, 2, 2]
    print(majority_element(input_elements,0,len(input_elements)))
