#sorting list

num = [6,1,8,4,3,9,7,1,5,6]
char=["d","a","y","c","g","l"]
print(num)
print( char)
num.sort()
char.sort()
print("Sort ascending order ",num)
print("sort ascending order ", char)

num.sort(reverse= True)
char.sort(reverse= True)
print("Sort descending order ",num)
print("sort descending order ", char)