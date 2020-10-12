d = {'British Raj': 200, 
' Mughal Empire': 350, 
'Delhi Sultanate': 100, 
'Maurya Vansh': 150}

sorted_d = sorted(d.items(), key = lambda x:x[1])
print("Sorted values:\n",sorted_d)
