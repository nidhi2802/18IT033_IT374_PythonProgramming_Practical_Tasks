import random
num = random.randint(1,9)
user_num = int(input("Enter a number: "))
if user_num<num:
    print("Your guess is too low")
elif user_num>num:
    print("Your guess is too high")
elif user_num==num:
    print("Your guess is exactly right")

print("The number is: ",num)
