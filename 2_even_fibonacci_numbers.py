# Problem: Even Fibonacci Numbers
# (https://projecteuler.net/problem=2)


cap = 4000000

def fib():
    fn_2 = 1
    fn_1 = 2
    yield 1
    yield 2
    while 1:
        fn = fn_2 + fn_1
        fn_2 = fn_1
        fn_1 = fn
        yield fn


acc = 0
for num in fib():
    if num > cap:
        break
    if num % 2 == 0:
        acc += num

print(acc)
