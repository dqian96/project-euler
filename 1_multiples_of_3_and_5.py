# Multiples of 3 or 5
# (https://projecteuler.net/problem=1)

# Simple single-pass to accumulate multiples of 3 and (multiples of 5 but not 3)


n = 1000

m3 = 3
m5 = 5
acc = 0

while m3 < n:
    acc += m3
    m3 += 3
    if m5 < n and m5 % 3 != 0:
        acc += m5
    m5 += 5

print(acc)
