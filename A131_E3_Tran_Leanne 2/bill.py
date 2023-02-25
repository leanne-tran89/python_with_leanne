#Leanne Tran
#2/13/23
#Exercise 3, Part 1

#This program calculates the amount of money that everyone has to pay, 
#including the tip after eating at a luxury restaurant

TIP = 0.15
BILL = 200
PARTY_OF_PEOPLE = 4

tipOfBill = BILL * TIP
tipPerPerson = tipOfBill / PARTY_OF_PEOPLE
billPerPerson = BILL / PARTY_OF_PEOPLE
totalCost = tipPerPerson + billPerPerson

print("The bill is $ " + str(BILL))
print("The tip is $ " + str(tipOfBill))
print("Each person has to pay $ " + str(totalCost))




