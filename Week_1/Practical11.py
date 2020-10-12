import random
number = random.randint(1, 9)
guess = 0
print("Guess a number between 1 and 9: ")
while guess < 5:

    guess_num = int(input())
    if guess_num == number:
        print("YOU WIN")
        break
    elif guess_num < number:
        print("Guess was low: Guess a number higher than", guess_num)
    else:
        print("Guess was high: Guess a number lower than", guess_num)
    guess += 1
if not guess < 5:
    print("YOU LOSE The number is", number)

