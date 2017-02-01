"""defining a method with variable no of arguments"""

#positional argument packing
def add(*nos):
	#print(type(nos)) is a tuple
	sum=0
	for n in nos:
		sum+=n
	return sum


print(add())
print(add(3,4))
print(add(5,6,7,8,9))

#argument unpacking
def two_adder(a,b):
	return a+b

l=[5,4]
#print (two_adder(l[0],l[1]))
print(two_adder(*l))

#keyword argument packing
def perimeter(**stats):
	#print(type(stats)) #dict
	return 2*(stats["length"]+stats["breadth"])

print(perimeter(length=6,breadth=3) )
print(perimeter(breadth=3,length=6) )

#print(perimeter(6,3)) #does not work
#print(perimeter(l=6,b=3)) #does not work


"""
KEYWORD ARGUMENT UNPACKING
s={"length":6,"breadth":3 }
#print(area(s["length"],s["breadth"]))
print(area(**s)) #keyword argument unpacking"""
