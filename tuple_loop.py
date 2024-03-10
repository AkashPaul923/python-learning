#tuple looping

a = ("Apple" , "Banana" , "Cheery" , "Dog" , "Lion" , "tiger" , "Deer")
print(a)

print("first methode")
for i in a:
    print(i)

print("second methode")
for j in range(len(a)):
    print(a[j])


print("third methode")
k = 0
while k < len(a):
    print(a[k])
    k+=1