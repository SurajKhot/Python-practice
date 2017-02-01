class CollegeUser(object):

	def __init__(self,name,gender):
		self.name=name
		self.gender=gender
	
	def display_details(self):
		print("{name}\n{gender}\n".format_map({"name":self.name,"gender":self.gender}) )
