student_details={}
print(type(student_details))

#add an item to the dictionary(key-value)
student_details[96]=("mehul",96,"m")
student_details[17]=("steve",17,"m")
student_details[25]=("katrina",25,"f")

#access a value from a dictionary
print(student_details[17])

#acces a value that does not exist by key

#check if whether key exists in dictionary or no
if 65 in student_details: #membership operator
	print(student_details[65])
else:
	print("not found")
	
	
#prints the list of all the keys in the dictionary
for s in student_details:
	print(s)

#print all the element(key-value) of a dictionary
items=student_details.items()
for item in items:
	print(str(item[0])+ "-"+ item[1][0])

#the number of entries in a dictionary
print(len(student_details) )

