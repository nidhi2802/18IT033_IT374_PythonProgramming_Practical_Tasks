num = int(input("Enter number to calculate its factorial: "))
fact = 1
if num<0:
  print("Factorial of negative number does'nt exist")
elif num==0:
  print("Factorial of 0 is ", fact)
else:
  for i in range (1, num+1):
    fact = fact*i
  
print("Factorial of {} is {}".format(num,fact))
