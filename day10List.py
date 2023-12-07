
namesList = ["M Hashim" , "Sabir" , "Shahab" , "Qasim" , "Ali" , "Dayan" , "Hayan"]
numbersList = [1, 2, 3, 4, 5, 6, 7, 8, 9,]

print(numbersList)
print(namesList)

namesList.append("Saad")
print(namesList)

namesList.sort()
print(namesList)

namesList.reverse()
print(namesList)

print(namesList[0:4])
print(namesList[2:-3])

print(numbersList.count(6))

numbersList.insert(2 , 44553)
print(numbersList)

exaple = [223, 554, 667]
numbersList.extend(exaple)
print(numbersList)

print(len(namesList))

for i in namesList:
    print(i,end=", ")

print('\n')
for i in range(len(namesList)):
    print(namesList[i])