import sys
p = int(sys.argv[1])
r = int(sys.argv[2])
n = int(sys.argv[3])
t = int(sys.argv[4])
amount = p*((1+(r/n))**(n*t))
com_interest = amount-p
print("Amount is: ", amount)
print("Compound interest is {}".format(com_interest))