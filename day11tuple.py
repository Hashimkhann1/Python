

countries = ("pakistan" , "india" , "china" , "saudi arabia" , "turkey")

print(countries)

####### we cannot change tuple value or not append any value to tuple
#### if we want to change or append value to tupple we need to convert the tuple into list and we can do anyting with list and then we will convert the list into tuple again

temp = list(countries)

temp.append("Russia")

countries = tuple(temp)

print(countries)
print(type(countries))