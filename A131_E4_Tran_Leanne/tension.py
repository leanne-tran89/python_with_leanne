#Leanne Tran
#2/22/23
#Exercise 4, Part D
from math import sqrt

#This program accepts a rotation speed v and determines whether such a speed 
#will cause the rope to break using formula: T = m v v / r

MASS = 2
LENGTH = 3
TENSION = 60

speed = int(input("Enter the rotation speed: "))

#greatest speed that rope can whirled without breaking
breakingPoint = sqrt((TENSION * LENGTH) / MASS)

if speed < breakingPoint:
    print("The rope does not break.")
else:
    print("The rope breaks.")