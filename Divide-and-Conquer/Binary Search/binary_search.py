# python3

import sys

def linear_search(keys, query):
    for i in range(len(keys)):
        if keys[i] == query:
            return i

    return -1


import math


# def binary_search(keys, query):
#     assert all(keys[i] < keys[i + 1] for i in range(len(keys) - 1))
#     assert 1 <= len(keys) <= 3 * 10 ** 4
#
#     # if true, return index, else return -1\
#
#     def bsearch(keys, left, right, query):
#
#         while left <= right:
#
#             mid = left + (right - left) // 2;
#             if keys[mid] == query:
#                 return mid
#
#             elif keys[mid] < query:
#                 left = mid + 1
#
#             else:
#                 right = mid - 1
#
#         return -1
#
#     # print("Hello")
#
#     return bsearch(keys, 0, (len(keys)-1), query)

def binary_search(keys, query):
    left, right = 0, len(keys) - 1

    while left <= right:
        mid = left + (right - left) // 2
        if keys[mid] == query:
            return mid
        elif query < keys[mid]:
            right = mid - 1
        else:
            left = mid + 1
    return -1


    

if __name__ == '__main__':
    input_keys = list(map(int, input().split()))[1:]
    input_queries = list(map(int, input().split()))[1:]
    for q in input_queries:
        print(binary_search(input_keys, q), end=' ')

    # keys = [1, 2, 3, 4, 5, 6, 7]
    # binary_search(keys, 7)


