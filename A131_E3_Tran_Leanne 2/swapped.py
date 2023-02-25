#Leanne Tran
#2/15/23
#Exercise 3, Part 4

# This program reads a string from a user and prints the string with the first
# and last character swapped
# (assume that user will enter a string with more than 2 characters)

word = input("Enter a string: ")

wordLen = len(word)
mid = wordLen // 2

if (wordLen % 2 == 0):
    p1 = word[0]
    p2 = word[1 : 3]
    p3 = word[wordLen - 1]

else:    
    p1 = word[0 : mid - 1]
    p2 = word[mid - 1: mid + 2]
    p3 = word[wordLen - 1]

print(p3 + p2 + p1)


