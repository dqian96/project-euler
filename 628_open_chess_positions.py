# Problem: Open Chess Positions
# (https://projecteuler.net/problem=628)

from collections import defaultdict
memoize = defaultdict(int)
memoize[0] = 1
memoize[1] = 1

mod = 1008691207

def fact(x):
    if x in memoize:
        return memoize[x]
    memoize[x] = (x * fact(x - 1))  % mod
    return memoize[x]


def solve2(n):
    ans = 0
    for x in range(1,n):
        ans += fact(x)
        ans %= mod

    ans *= 2
    ans += 1

    doubleblocks = 0
    for x in range(n-1):
        doubleblocks += fact(x) * (n-x-1)
        doubleblocks %= mod
    return (fact(n) - (ans - doubleblocks)) % mod
