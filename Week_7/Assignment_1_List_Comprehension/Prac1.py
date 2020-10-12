import sys
x1 = int(sys.argv[1])
series = []
series.append(1)
series.append(1)
if x1 == 0:
    print("Fibonacci Series with n=0 does'nt exist")
elif x1 == 1:
    print("Fibonacci Series with n=1: ", series[0])
else:
    [series.append(series[k - 1] + series[k - 2]) for k in range(2, x1)]
    print("Fibonacci Series with n={}: {}".format(x1,series))
