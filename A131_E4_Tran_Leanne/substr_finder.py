#Leanne Tran
#2/22/23
#Exercise 4, Part E

#This program finds the number of times the following substrings appear in
#the text
# “un”
# “an”
# “in”
# “he

string = "Debating me breeding be answered an he. Spoil event was words her off cause any. Tears woman which no is world miles woody. Wished be do mutual except in  effect answer. Had friendship thoroughly cultivated son hills day ten. Examine waiting his evening day passage proceed."

print("In the following paragraph: ")
print()

print("----------------------------------------------------------------------")

print("Debating me breeding be answered an he. Spoil event was words her")
print("off cause any. Tears woman which no is world miles woody. Wished be do")
print("mutual except in effect answer. Had friendship thoroughly cultivated son")
print("hills day ten. Examine waiting his evening day passage proceed.")

print("----------------------------------------------------------------------")
print()

unCount = str(string.count("un"))
unFind = str(string.find("un"))
print(" \"un\" appears in the text " + unCount + " time(s) and the lowest index of the first occurrence of \"un\" is at index "+ unFind)

anCount = str(string.count("an"))
anFind = str(string.find("an"))
print(" \"an\" appears in the text " + anCount + " time(s) and the lowest index of the first occurrence of \"an\" is at index "+ anFind)

inCount = str(string.count("in"))
inFind = str(string.find("in"))
print(" \"in\" appears in the text " + inCount + " time(s) and the lowest index of the first occurrence of \"in\" is at index "+ inFind)

heCount = str(string.count("he"))
heFind = str(string.find("he"))
print(" \"he\" appears in the text " + heCount + " time(s) and the lowest index of the first occurrence of \"he\" is at index "+ heFind)

              



