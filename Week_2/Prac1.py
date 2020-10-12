operator = int(input("Enter: \n 1 for arithmetic operations\n 2 for Assignment operator \n 3 for comparison operations \n 4 for logical operations \n 5 for bitwise operations \n 6 for identity operations \n 7 for membership operations\n"))

if(operator==1):
  op1 = int(input("Enter operand 1: "))
  op2 = int(input("Enter operand 2: "))
  add = op1+op2;
  sub = op1-op2;
  mul = op1*op2;
  div = op1/op2;
  exp = op1**op2;
  print("Addition of {} and {} is {}".format(op1, op2, add));
  print("Subtraction of {} and {} is {}".format(op1, op2, sub));
  print("Multiplcation of {} and {} is {}".format(op1, op2, mul));
  print("Division of {} and {} is {}".format(op1, op2, div));
  print("{} power {} is {}".format(op1, op2, exp));

if(operator== 2):
  a = 2
  c = 3
  print("Value of a is {} and value of c is {}".format(a,c));
  c+=a
  print("Value of c+=a is ",c)
  c*=a
  print("Value of c*=a is ",c)
  c**=a
  print("Value of c**=a is ",c)

if(operator==3):
  op1 = int(input("Enter operand 1: "))
  op2 = int(input("Enter operand 2: "))
  if(op1==op2):
    print("Operand 1 and operand 2 are equal")
  if(op1>op2):
    print("Operand 1 is greater than operand 2")
  if(op1<op2):
    print("Operand 1 is less than operand 2")
  if(op1>=op2):
    print("Operand 1 is either greater than or equal to operand 2")
  if(op1<=op2):
    print("Operand 1 is either lesser than or equal to operand 2")

if(operator == 4):
  op1 = int(input("Enter operand 1: "))
  op2 = int(input("Enter operand 2: "))
  add = op1+op2
  mul = op1*op2
  if(add and mul):
    print("Addition and multiplication of Operand 1 and operand 2 are equal")
  else:
    print("Addition and multiplication of Operand 1 and operand 2 is 0")
  if(add or mul):
    print("Either or both Addition and multiplication of operand 1 and operand 2 is non zero")
  else:
    print("Both Addition and multiplication of Operand 1 and operand 2 is 0")

if(operator==5):
  op1 = int(input("Enter operand 1: "))
  op2 = int(input("Enter operand 2: "))
  print("Bitwise and: ", (op1&op2))
  print("Bitwise or: ", (op1|op2))
  print("XOR: ", (op1^op2))
  print("{}'s complement: {}".format(op1, (~op1)))
  print("Binary right shift on operand 2: ",(op2>>2))

if(operator == 6):
  op1 = int(input("Enter operand 1: "))
  op2 = int(input("Enter operand 2: "))
  if(op1 is op2):
    print("Operand 1 and operand 2 have same identity")
  
  if(op1 is not op2):
    print("Operand 1 and operand 2 do not have same identity")

if(operator == 7):
  op1 = int(input("Enter operand 1: "))
  op2 = int(input("Enter operand 2: "))
  list1 = [1, 2, 3, 4, 5]
  if(op1 in list1):
    print("Operand 1 is present in list")
  else:
    print("Operand 1 is not present in list")
  if(op2 in list1):
    print("Operand 2 is present in list")
  else:
    print("Operand 2 is not present in list")