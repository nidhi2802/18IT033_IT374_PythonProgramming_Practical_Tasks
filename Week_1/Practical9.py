num = int(input("Enter number upto which you want find prime numbers: "))
for x in range(num+1):
    if x>1:
        for i in range(2, x):
            if(x%i==0): 
                break
        else:
            print(x)
