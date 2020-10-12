import sys
number = int(sys.argv[1])
sum = 0
for i in range(1, number):
    if(number%i==0):
        sum = sum+i

if(sum==number):
    print("{} is a perfect number".format(number))
else:
    print("{} is not a perfect number".format(number))
    