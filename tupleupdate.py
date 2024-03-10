#Tuple Update
fruits = ("Apple" , "Banana" , "Cheery")
print(fruits)
f=list(fruits)
f.append("Doll")
f.append("Eagle")
fruits=tuple(f)

print(fruits)
print(type(fruits))