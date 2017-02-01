def display_details(n,r,g):
	print("Name: "+n)
	print("Roll no: "+str(r))
	print("Gender "+g)
	
def calculategrade(marks):
	marks=float(input("Enter marks: "))
	if marks >=70 and marks<=100:
		print("Grade A")
	elif marks >=60 and marks<=70:
		print("Grade B")
	elif marks >=50 and marks<=60:
		print("Grade c")
	elif marks <40 and marks>=0:
		print("Fail")
	else:
		print("Invalid")
