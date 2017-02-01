#import patterns
#import math

from com.example.custom.patterns import fibo
from com.example.custom.math import evenodd as eo #given an alias
while True:
	print("1. Fibonacci Series")
	print("2. Even odd")
	print("3. Exit")
	
	choice=int(input("Enter choice from 1 to 3: "))

	
	if choice==1:
		n=int(input("Enter: "))
		fibo(n)

	elif choice==2:
		n=int(input("Enter: ")) 	
		eo(n)
	else:
		break

