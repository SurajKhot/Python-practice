from collegeuser import CollegeUser

class Student(CollegeUser):

	def __init__(self,name,gender,roll,marks):
		 super().__init__(name,gender)
		 self.roll=roll
		 self.marks=marks
	
	def get_name_roll(self): #t=tuple where the elements are of heterogenous types
		t=(self.name,self.roll)
		return t
		 
	def display_details(self):
		"""print("Name: "+self.name")
		print("Gender "+self.gender)))"""
		"""
		print("Name: ",self.name,"\n Gender: ",self.gender)
		#print("Roll no: "+str(self.roll))
		print("Roll no: ",self.roll)
		"""
		#print("Name: {0}\n Gender: {1}\nRoll No: {2}".format(self.name,self.gender,self.roll))
		
		#print("{name}\n{gender}\n{roll}".format_map({"name": self.name,"gender": self.gender,"roll": self.roll}))
		super().display_details()
		print("roll no: {0} ".format(self.roll))
		
		
	def calculate_grade(self):
		marks=self.marks
		marks=float(input("Enter marks: "))
		if marks >=70 and marks<=100:
			print("Grade A")
		elif marks >=60 and marks<=70:
			print("Grade B")
		elif marks >=50 and marks<=60:
			print("Grade c")
		elif marks <40 and marks>=0:
			print("Fail")
			print("Invalid")
