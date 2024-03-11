set1 = {1,2,3,4,5}
set2 = {"apple","banana","cheery"}
print(set1)
print(set2)
#set looping
for i in set2:
    print(i)


#join two set using union() function
set3 = set2.union(set1)
print(set3)

#join two set using union() function
set1.update(set2)
print(set1)

