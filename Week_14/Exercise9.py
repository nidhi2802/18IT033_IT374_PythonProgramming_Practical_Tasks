def file_list(file):
	list1 = []
	with open(file) as f:
		line = f.readline()
		while line:
			list1.append(int(line))
			line = f.readline()
	return list1


prime_list = file_list('Primes.txt')
happy_list = file_list('HappyNumbers.txt')

list2 = [num for num in prime_list if num in happy_list]
print(list2)
