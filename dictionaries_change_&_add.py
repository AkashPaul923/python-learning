# define dictionaries
studentinfo = {
    "Name" : "Akash Paul",
    "Roll" : 20078,
    "Dept" : "CSE",
    "See." : "2020-21",
    "YOB" : 2000
}
print(studentinfo)

#change item 1st methode
studentinfo["Roll"] = 21078
print(studentinfo)

#change item using update() function
studentinfo.update({"YOB": 2002})
print(studentinfo)

#add item 1st methode
studentinfo["Address"] = "Dhaka"
print(studentinfo)

#Add item using update() function
studentinfo.update({"Institute" : "IST"})
print(studentinfo)



