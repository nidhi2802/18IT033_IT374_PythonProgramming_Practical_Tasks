def countNotes(amount):
    notes = [2000, 500, 200, 100, 50, 20, 10, 5, 1]
    notes_counter = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    print("Note count: ")
    for i,j in zip(notes, notes_counter):
        if(amount>=i):
            j = amount//i
            amount = amount - j*i
            print(i, "->", j)

amt = int(input("Enter amount to calculate minimum number of currency notes required: "))
countNotes(amt)