#Leanne Tran
#2/22/23
#Exercise 4, Part B

# This program asks the user whether the increasing/decreasing should be strict 
# or lenient. Lenient mode allows the sequence 3 4 4 to be increasing and the
# sequence 444 to be both increasing and decreasing

type = input("Do you want strict or lenient? ")

first = int(input("Enter the first number: "))
second = int(input("Enter the second number: "))
third = int(input("Enter the third number: "))

if (type == "lenient"):
    if ((first < second and second < third) or (first < second and second == third)):
        print("They are in increasing order.")   
    elif ( first == second == third): 
        print("They are in both increasing order and decreasing order.")
    else:
        print("They are in decreasing order.")
        

if (type == "strict"):
    if (first < second and second < third):
        print("They are in increasing order.")
    elif (first > second and second > third):
        print("They are in decreasing order.")
    else:
        print("They are neither in increasing order nor decreasing order.")        
    


#lenient mode

#increasing
# first < second < third
# first < second == third
# first == second == third

#decreasing
#first > second > third

#else:
#neither



#strict mode

#increasing
#first < second < third

#decreasing
#first > second > third

#else:
#neither

    
