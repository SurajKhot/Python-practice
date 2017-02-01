student1=("mehul","1","m")
print(type(student1))  #tuple

for s in student1:
	print(s)
	
#access an element of a tuple
print(student1[1])

#tuple unlinke list,is immutable
#student1[0]="mehul" #gives an error
#Tuple is a fast list

#single element tuple
s=("mehul",)
print(type(s))

#convert a list to a tuple
nos=[3,4,5]
t=tuple(nos)
print(t)
