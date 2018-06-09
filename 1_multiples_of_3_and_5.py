# Multiples of 3 or 5
# (https://projecteuler.net/problem=1)

# Simple single-pass to accumulate multiples of 3 and (multiples of 5 but not 3)


# n = 1000

# m3 = 3
# m5 = 5
# acc = 0

# while m3 < n:
#     acc += m3
#     m3 += 3
#     if m5 < n and m5 % 3 != 0:
#         acc += m5
#     m5 += 5

# print(acc)

"""
    There exists a closed form solution to this question.

    Notice that for the sum of multiples of a given number x, you can factor out x to get a arithmetic series
    from 1 to n. We know the formula for this series as n(n + 1)/2.

    We let n = floor((cap - 1)/x), since it is the largest number of multiples of x below cap.

    In the particular cases of 3 and 5, we can first calculate the sum of multiples of 3 and 5. Note that in this
    case we are DOUBLE COUNTING the multiples of 3 AND 5. Thus, we have to subtract the sum of multiples of 15.

    Thus SumMultiples(3 or 15) = SumMultiples(3) + SumMultiples(5) - SumMultiples(15)
"""

N = 1000

def sum_multiples(cap, x):
    n = int((cap - 1)/x)
    return int(x * n * (n + 1) / 2)

def ans(n1, n2):
    return sum_multiples(N, n1) + sum_multiples(N, n2) - sum_multiples(N, n1 * n2)

print(ans(3, 5))
