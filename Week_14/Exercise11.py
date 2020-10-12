import json
dict_birthday = {}
with open('birthdayslist.json','r') as f:
    dict_birthday = json.load(f)

def find_birthday():
    user_input = input("Who's birthday do you want to know? ")
    try:
        if dict_birthday[user_input]:
            print("{}'s birthday is on {}".format(user_input, dict_birthday[user_input]))
    except KeyError:
        print("{} is not in the list".format(user_input))

def print_birthday():
    print("Welcome to the birthday dictionary. We know the birthdays of: ")
    for i in dict_birthday:
        print(i, ':', dict_birthday[i])

print_birthday()
while True:
    choice = input("\nWhat you want to do next:Find, Quit\n")
    if choice == 'Quit':
        print("Good Bye")
        raise SystemExit(0)
    elif choice == 'Find':
        find_birthday()
    else:
        print("You have entered invalid choice")
