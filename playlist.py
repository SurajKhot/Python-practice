cars=["mercedes","audi","bmw"]
print(type(cars))

#ordered collection of elements
print(cars[0])
print(cars[2])

#modify a element on the list
cars[0]="Mercedes"
print(cars[0])

#no of elements in a list
print(len(cars))

#access the last element of a list
print(cars[len(cars)-1])

#add an element at the end of the list
cars.append("nano")
print(cars)

#add more than one element at the end of the list
cars.extend(["i20","i10"])
print(cars)

#add an element at a specific position in the list
cars.insert(1,"Porsche")
print(cars)

#remove an element from the end of the list
print(cars.pop())
print(cars)

#remove an element from a specific position of the list
print(cars.pop(2))
print(cars)

#print all the elements of a list
for car in cars:
	print(car)
	
#sorting the elements in ascending order
"""cars.sort()
print(cars) """

#sort the elements in descending order
"""cars.reverse()
print(cars)"""

cars.sort(reverse=True)
print(cars)

#list with squares of all elements

nos=[1,2,3,4,5,6,7,8,9]
"""n2=[]
for n in nos:
	n2.append(n**2)"""
	
n2=[n**2 for n in nos]	
print(n2)

#new list with the squares of all even elements from old list 
n3=[n**2 for n in nos if n%2==0]
print(n3)

n4=[n**3 for n in nos if n%2==0 and n>4]
