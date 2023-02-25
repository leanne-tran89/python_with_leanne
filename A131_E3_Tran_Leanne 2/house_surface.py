#Leanne Tran
#2/13/23
#Exercise 3, Part 2

#This program estimates the cost of painting a house by first calculating the
#surface area of the exterior

HOUSE_WIDTH = 23
HOUSE_LENGTH = 45
HOUSE_HEIGHT = 9.5

WINDOWS = 12
WINDOWS_WIDTH = 3
WINDOWS_HEIGHT = 3.5

DOORS = 4
DOORS_WIDTH = 3
DOORS_HEIGHT = 7.5

# RECTANGULAR PRISM SA = 2(HL + HW)
houseSA = 2 * ((HOUSE_WIDTH * HOUSE_HEIGHT) + (HOUSE_HEIGHT * HOUSE_LENGTH))

#windows
windowsSA = WINDOWS_WIDTH * WINDOWS_HEIGHT
totalWindowsSA = windowsSA * WINDOWS

#doors
doorsSA = DOORS_WIDTH * DOORS_HEIGHT
totalDoorsSA = doorsSA * DOORS

#calculate
surfaceArea = houseSA - totalWindowsSA - totalDoorsSA


print("The surface area to be painted of a house is " + str(surfaceArea) + " sqft.")
