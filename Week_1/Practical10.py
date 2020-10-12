def Fibonacci(num):
	if num<0:
		print("Incorrect input")
	elif num==0:
		return 0
	elif num==1:
		return 1
	else:
		return Fibonacci(num-2)+Fibonacci(num-1)


num = int(input("Enter number of elements upto which you want Fibonacci series: "))
print("Fibonacci Series: ")
for i in range(0,num):
    print(Fibonacci(i))
