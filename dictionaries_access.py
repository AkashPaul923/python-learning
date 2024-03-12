# define dictionaries
studentinfo = {
    "Name" : "Akash Paul",
    "Roll" : 21078,
    "Dept" : "CSE",
    "See." : "2020-21"
}
#print whole dict..
print(studentinfo)

#access specific value
print(studentinfo["Roll"])

#access value using get() function
x= studentinfo.get("Name")
print(x)

#access all keys using keys() function
y= studentinfo.keys()
print(y)

#access all values using values() function
z= studentinfo.values()
print(z)
