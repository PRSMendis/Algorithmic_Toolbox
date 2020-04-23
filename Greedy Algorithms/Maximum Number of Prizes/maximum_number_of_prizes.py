# python3


def compute_optimal_summands(n):
    assert 1 <= n <= 10 ** 9
    summands = []

    # greedy solution
    # takes in number, check if the number input is greater than the previous number, if so coutn +=1
    # else, return difference

    def counter(n):
        s = 0
        i = 1
        while s + i <= n:
            if s <= n:
                #             if s <=n and s+i+1 < n:
                summands.append(i)
                s += i
                i += 1
        #             else:
        #                 summands.append(n-s)
        #         return i-1, summands[0:-1]
        summands[-1] += n - sum(summands)
        return summands

    counter(n)

    #     return len(summands), summands, sum(summands)
    return summands



if __name__ == '__main__':
    input_n = int(input())
    output_summands = compute_optimal_summands(input_n)
    print(len(output_summands))
    print(*output_summands)
