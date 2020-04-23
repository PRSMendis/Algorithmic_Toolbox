# python3

from collections import namedtuple
import collections
from sys import stdin
import numpy as np

Segment = namedtuple('Segment', 'start end')


def compute_optimal_points(segments):
    def l_dict(M):
        d = {}
        for i, l in enumerate(M):
            #         print(i, l)
            for j, num in enumerate(l):
                #                 print(j, num)
                if num not in d:
                    d[num] = 1
                else:
                    d[num] += 1
        return {k: v for k, v in sorted(d.items(), key=lambda item: item[1], reverse=True)}

    #     print("Hello World")

    # print(len(segments))
    #     M = [[]* len(segments)]
    M = [[] for _ in range(0, len(segments))]
    #     print(M[0])

    # e
    for i, segment in enumerate(segments):
        M[i] = [num for num in range(segment.start, segment.end + 1)]

    #     return M
    l_d = l_dict(M)
    l_l = list(l_d)
    #     return l_dict(M)

    ############# with the sorted dictionary and list, read from it and use it to delete any list with the variable #####################
    val = l_l[0]

    def drow(M, v, count=0):
        i = 0
        #         print(len(M))
        while i < len(M):
            #             print("M,i = " + str(M),i)
            for j, num in enumerate(M[i]):
                #                 print(i, num,v)
                if num == v:
                    #                     print("YA")
                    del M[i]
                    i -= 1
            #                 count+=1
            i += 1

        return M, count

    #     return drow(M,val) == []
    k = 0
    v = []
    count = 0
    while M != []:
        l = list(l_dict(M))[0]
        v.append(l)
        M, count = drow(M, v[k], count)
        k += 1
    return v





if __name__ == '__main__':
    n, *data = map(int, stdin.read().split())
    input_segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    assert n == len(input_segments)

    # s = ([Segment(1, 3), Segment(2, 5), Segment(3, 6)])
    #
    # output_points = compute_optimal_points(s)
    output_points = compute_optimal_points(input_segments)
    # print(output_points)




    print(len(output_points))
    print(*output_points)
