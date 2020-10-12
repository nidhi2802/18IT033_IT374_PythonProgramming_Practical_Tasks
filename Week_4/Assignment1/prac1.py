row = int(input("Input number of rows: "))
col = int(input("Input number of columns: "))
multi_list = [[0 for cols in range(col)]for rows in range(row)] 

for rows in range(row):
    for cols in range(col):
        multi_list[rows][cols]= rows*cols*33
print(multi_list)
