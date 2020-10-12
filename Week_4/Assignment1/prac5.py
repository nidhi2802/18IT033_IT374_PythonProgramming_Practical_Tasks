string = input("Enter string")
digit=0
letter=0
for i in string:
  if i.isalpha():
        letter=letter=1
  elif i.isdigit():
        digit=digit+1
  else:
        pass
print("Letters", letter)
print("Digits", digit)
