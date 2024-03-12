studentinfo = {
    'Name': 'Akash Paul',
    'Roll': 21078,
    'Dept': 'CSE',
    'See.': '2020-21',
    'YOB': 2002,
    'Address': 'Dhaka',
    'Institute': 'IST'
}
print(studentinfo)

#remove item using pop() function
studentinfo.pop("YOB")
print(studentinfo)

#remove item using popitem() function....it removes last item
studentinfo.popitem()
print(studentinfo)

#remove item using del keyward
del studentinfo["Roll"]
print(studentinfo)

#remove item using clear() function.....it removes all item
studentinfo.clear()
print(studentinfo)

#remove dictionary using del keyward....it delete the dictionary
del studentinfo

