ages=[20,21,20,25,24,23]

#only unique elements in the data structure
unique_ages=set(ages)
print(unique_ages)
print(type(unique_ages))

#manually create a set
fruits={"banana","chicku","apple","chicku","mango"}
print(fruits)

#unordered set of elements so u cant access using index

#printing all elements of a set
for f in fruits:
	print(f)

#mathematical set
a={1,3,4,7}
b={3,5,8}

print(a-b) #elements in a but not in b
print(a & b) #intersection
print(a|b) #union
print(a^b) #

#empty set
e={}
print(type(e)) #creates a dictionary

e=set() #empty set
print(type(e))

#add an element to a set
e.add(4)
e.add(3)
e.add(4)
e.add(5)
print(e)
