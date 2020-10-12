num = int(input("Enter number N upto which find odd and even numbers "))
for x in range(num+1):
    if(x%2==0):
        print(x, " is even number")
    else:
        print(x, " is odd number")