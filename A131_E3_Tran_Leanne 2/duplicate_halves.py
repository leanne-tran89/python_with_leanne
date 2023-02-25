#Leanne Tran
#2/15/23
#Exercise 3, Part 5

# This program reads a string from the user and prints the string with the 
# first half and second half doubled
# (assume that user is entering a string with even numbers)

word = input("Enter a string: ")
wordLen = len(word)
mid = wordLen // 2

p1 = word[0: mid]
p2 = word[mid: wordLen]

doubleFirst = p1 + p1
doubleLast = p2 + p2

final = doubleFirst + doubleLast
print(final)