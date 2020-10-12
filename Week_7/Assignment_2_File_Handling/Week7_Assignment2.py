import csv
file1 = open('Output.txt','w')
with open('Practical7.csv','rt') as file:
    for row in file:
        file1.write(row.replace(","," "))
 
file1.close
