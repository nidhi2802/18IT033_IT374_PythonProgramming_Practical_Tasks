list1 = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
list2 = [list1[i] for i in range (len(list1)) if list1[i]<5]
print(list2)
