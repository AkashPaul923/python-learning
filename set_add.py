set1 = {1,2,3,4,5}
set2 = {"apple","banana","cheery"}
print("set 1 : ",set1)
print("set 1 : ",set2)

#add 1 value in set using add() function
set1.add(6)
print("after add 1 value in set 1 : ",set1)

#add 1 set into another set using update() function
set1.update(set2)
print("after add set 2 value in set 1 : ",set1)