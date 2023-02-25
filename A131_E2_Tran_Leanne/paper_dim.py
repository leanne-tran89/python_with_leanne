from math import sqrt
#This program computes and displays the perimeter of a letter-size (8.5 × 11 inch)
#sheet of paper and the length of its diagonal
#Leanne Tran
#2/6/23
#Exercise 2, Part 2

#perimeter: 2 ( l + w)
#diagonal: sqrt(w ^ 2 + h ^ 2)


width = 8.5
height = 11

perimeter = (2 * (height + width))
perimeter1 = (str)(perimeter)
diagonal = sqrt((width ** 2) + (height** 2))
diagonal1 = (str)(diagonal)

print("The perimeter is " + perimeter1 + " inches.")
print("The length of the diagonal is  " + diagonal1 + " inches.")
