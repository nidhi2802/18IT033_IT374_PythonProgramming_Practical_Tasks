choice = int(input("To covert rupees to dollar- enter 1 and to convert dollar to rupees - enter 2 "))
if(choice==1):
    amt_rupees = float(input("Enter amount in rupees: "))
    cnv_dollar = amt_rupees/70
    print(amt_rupees, "rupees is equal to ", cnv_dollar, "dollar/s")
elif(choice==2):
    amt_dollar = float(input("Enter amount in dollar: "))
    cnv_rupees = amt_dollar*70
    print(amt_dollar, "dollar/s is equal to ", cnv_rupees, "rupees")
else:
    print("You have entered invalid choice")
