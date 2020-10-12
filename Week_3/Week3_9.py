num = int(input("Enter number of elements upto which you want Fibonacci series: "))
n1 = 0
n2 = 1
count = 0
if num<=0:
  print("Enter number greater than 0")
elif num==1:
  print("Fibonacci Series upto 1 term: ", n1)
else:
  print("Fibonacci series upto {} terms: ".format(num))
  while count<num:
    print(n1, end=' ')
    n3 = n1+n2
    n1 = n2
    n2 = n3
    count+=1
  