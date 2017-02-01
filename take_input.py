    print("program starts")

for n in range(0,4):
	n1=input("enter n: ")
	try:
		n2=int(n1)
	except ValueError:
		print("please enter a proper value")
	else:
		print("value taken is {0}".format(n2))
		break
print("program ends")
