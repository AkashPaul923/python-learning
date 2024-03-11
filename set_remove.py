set1 = {1,2,3,4,5,"apple","banana","cheery"}
print(set1)

#remove item using remove() function
set1.remove("banana")
print(set1)

#remove item using discard() methode....this function doesnot give error if item deesnot esist
set1.discard(5)
print(set1)

#remove item using pop() function
set1.pop()
print(set1)

#remove item using clear() function
set1.clear()
print(set1)

#The del keyword will delete the set completely:
del set1