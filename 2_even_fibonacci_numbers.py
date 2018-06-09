# Problem: Even Fibonacci Numbers
# (https://projecteuler.net/problem=2)


# cap = 4000000

# def fib():
#     fn_2 = 1
#     fn_1 = 2
#     yield 1
#     yield 2
#     while 1:
#         fn = fn_2 + fn_1
#         fn_2 = fn_1
#         fn_1 = fn
#         yield fn


# acc = 0
# for num in fib():
#     if num > cap:
#         break
#     if num % 2 == 0:
#         acc += num

# print(acc)



"""
    Another observation we could make is that every 3rd number in the fibonacci sequence is even.
    Let us prove that f(n) is even when n % 3 == 0 and odd otherwise.

    Base cases:

    f(1) = 1
    f(2) = 1
    f(3) = 1 + 1 = 2

    Thus, we have proven our proposition true for n = 1 to 3.

    Inductive Assumption: Let us assume that f(k) follows our proposition for n <= k.
    Prove f(k + 1), f(k + 2), f(k + 3) follows our proposition.

    Proof:

    Case 1:
    Let us assume the case when k % 3 == 0.
    Then, according to our proposition f(k) % 2 == 0 and f(k - 1) % 2 == 1.

    By the linearity of mod, we know that
    f(k + 1) mod 2 = f(k) mod 2 + f(k - 1) mod 2.
    f(k + 1) mod 2 = (0 + 1) mod 2 = 1 and so f(k + 1) is an odd number.

    Using the same logic:

    f(k + 2) mod 2 = f(k + 1) mod 2 + f(k) mod 2 = (1 + 0) mod 2 = 1
    f(k + 3) mod 2 = f(k + 2) mod 2 + f(k + 1) mod 2 =  (1 + 1) mod 2 = 0

    Case 2:
    The inductive hypothesis holds by the same logic as the previous case.


    Thus, since f(k + 1), f(k + 2), f(k + 3) hold given that f(k) is true and the base cases are true, we have
    proven that our proposition is true.
"""

cap = 4000000

a = 1
b = 1
c = 2

s = 0

while c < cap:
    s += c
    a = b + c
    b = a + c
    c = a + b

print(s)
