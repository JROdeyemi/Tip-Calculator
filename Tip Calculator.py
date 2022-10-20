print('Welcome to the tip Calculator! ')
Bill = input('How much is your bill \n $')
Tip = input('How much tip (%) would you like to give? 10, 12 or 15 \n ')
People = input('How many people are splitting the bill? \n ')

Billamount= float(Bill)
Tipamount = ((int(Tip)) / 100)
Peopleamount = int(People)

Totalcost = ((Billamount * Tipamount) + Billamount)
Personalcost = round(float(Totalcost / Peopleamount), 2)
print(f'Cost per person is ${Personalcost}')