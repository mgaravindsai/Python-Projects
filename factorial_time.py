import timeit

def fact(n):
    if n == 1:
        return 1
    else:
        return n * fact(n-1)

def num(n):
    m = 1
    for i in range(1,n+1):
        m *=i
    return m


f = timeit.Timer("x","from __main__ import x")
x = fact(900)
pt = f.timeit(number=1000)
print(x,pt)
x = num(100000000)
pts = f.timeit(number=1000)
print(x,pts)