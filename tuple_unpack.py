#unpack touple

# 1st methode
fruits = ("Apple" , "Banana" , "Cheery")
print(fruits)

(a,b,c) = fruits
print(a)
print(b)
print(c)

#2nd methode
animals = ("Dog","Lion","tiger","Deer")
print(animals)

( x,*y) = animals
print(x)
print(y)