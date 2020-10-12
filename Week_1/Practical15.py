def Swap(a,b):
    print("Before swapping:\nvalue of a is ",a,"\nvalue of b is ",b)
    temp = b
    b = a
    a = temp
    print("After swapping:\nvalue of a is ", a, "\nvalue of b is ", b)


a = input("Enter number 1: ")
b = input("Enter number 2: ")
Swap(a,b)