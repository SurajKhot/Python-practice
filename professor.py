from collegeuser import CollegeUser

class Professor(CollegeUser):

	def __init__(self,name,gender,sub):
		 super().__init__(name,gender)
		 self.sub=sub
		 
			 
	def display_details(self):
		super().display_details()
		if len(self.sub)==0:
			print("no subjects")
		else:
			for sub in self.sub:
				print(sub)

