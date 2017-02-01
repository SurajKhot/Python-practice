#this is an example of a comment
def area(l=2,b=1):
	return l*b
def perimeter(l,b):
	return 2*(l+b)

"""multi line comments""" 
"""
print(area())
print(area(4))
print(area(4,2))

print(perimeter(l=3,b=4)) 
print(perimeter(b=1,l=2))
"""

length=int(input("enter length: "))
breadth=int(input("enter breadth: 	"))

a=area(length,breadth)
p=perimeter(length,breadth)

print("Area is " +str(a))
print("Perimeter is " +str(p))
