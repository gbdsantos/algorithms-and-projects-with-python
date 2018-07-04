import timeit

'0-1-2-3-.....-99'

timeit.timeit(' "-".join(str(n) for n in range(100))', number=10000)

timeit.timeit(' "-".join([str(n) for n in range(100)])', number=10000)

timeit.timeit(' "-".join(map(str, range(100)))')

%timeit "-".join(str(n) for n in range(100))
%timeit "-".join([str(n) for n in range(1
%timeit "-".join(map(str, range(100)))