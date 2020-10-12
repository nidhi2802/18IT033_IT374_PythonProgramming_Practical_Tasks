import sys
x1 = int(sys.argv[1]);
x2 = int(sys.argv[2]);
for i in range (x1, x2+1):
  if(i%3==0 and i%5==0):
    print("{} is divisble by 3 and multiple of 5".format(i))

