#Leanne Tran
#2/22/23
#Exercise 4, Part A

# This program reads 3 numbers and prints "increasing" if they are in increasing
# order, "decreasing" if they are in decreasing order, and "neither" otherwise


first = int(input("Enter the first number: "))
second = int(input("Enter the second number: "))
third = int(input("Enter the third number: "))

if (first < second and second < third ):
    print("They are in increasing order.")
elif (first > second and second > third):
        print("They are in decreasing order.")
else:
    print("They are neither in increasing order nor decreasing order.")

