from collections import Counter 
list1 = [1, 2, 3, 2, 2, 2, 5, 6]
counter = 0
num = list1[0]
for i in list1:
  current = list1.count(i)
  if(current>counter):
    counter=current
    num=i
print("Most common element in list: ",num)
print("Count of element in list: ", counter)
tuples = ("apple", 2, 3,"apple","apple", "apple", 5, 6)
counter_t = 0
num_t = tuples[0]
for j in tuples:
  current_t = tuples.count(j)
  if(current_t>counter_t):
    counter_t=current_t
    num_t=j
print("Most common element in tuple: ",num_t)
print("Count of element in tuple: ", counter_t)
dict1={
  "one": 1,"two": 2,  "two2": 2, "two3": 2, "three": 4, "three3": 4
}
res = Counter(dict1.values())
print("The frequency dictionary : " + str(dict(res))) 