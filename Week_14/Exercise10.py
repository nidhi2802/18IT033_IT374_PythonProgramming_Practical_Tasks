dict_birthday = {
    "Mahatma Gandhi" : "2nd October",
    "Sardar Vallabbhai Patel": "31st October",
    "Jawaharlal Nehru": "14th November",
    "Subhash Chandra Bose": "23rd January",
    "Rajendra Prasad": "3rd December"
}
print("Welcome to the birthday dictionary. We know the birthdays of: ")
for i in dict_birthday:
    print(i)
user_input = input("Who's birthday do you want to know? ")
try:
    if dict_birthday[user_input]:
        print("{}'s birthday is on {}".format(user_input,dict_birthday[user_input]))
except KeyError:
    print("{} is not in the list".format(user_input))
