#list comprehension


numbers= [1,2,3,4,5,6,7,8,9] #list define
add = [i+9 for i in numbers]
sub = [i-1 for i in numbers]
multi = [i*5 for i in numbers]
div = [i/2 for i in numbers]
pow = [i**i for i in numbers]

print("Before : ",numbers)
print("After Addition 9 : ",add)
print("After Subtraction 1 : ",sub)
print("After Multiplication 5 : ",multi)
print("After Division 2 : ",div)
print("After Power : ",pow)