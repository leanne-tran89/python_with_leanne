#Leanne Tran
#2/22/23
#Exercise 4, Part C

#Write a program that reads in a string and whether it
# contains only letters. = isalpha()
# contains only uppercase letters. = isupper()
# contains only lowercase letters. = islower()
# contains only digits. = isdigit()
# starts with an uppercase letter. = isupper() and check first index
# ends with a period. = endswith(value, start, end)


userInput = input("Enter a string: ")

if (userInput.isalpha()):
    print("The string contains only letters.")

if (userInput.islower()):
    print("All letters in the string are lowercase letters.")
elif (userInput.isupper()):
    print("All letters in the string are uppercase letters.")

if (userInput.isdigit()):
    print("The string contains only digits.")

if (userInput[0].isupper()):
    print("The string starts with an uppercase letter.")
    
if (userInput.endswith(".")):
    print("The string ends with a period.")
    
    
    
    

