listbinary = []
three = '00011'
num = [x for x in input().split(',')]
for i in num:
    x = int(i, 2)
    if  (x%7==0):
        sum = str(bin(int(i,2)+int(three,2)))
        listbinary.append(sum[2:])
print(','.join(listbinary))
