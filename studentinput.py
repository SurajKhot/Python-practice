#import student_ops

from student import Student


name=input("Enter the name: ")
roll=int(input("Enter roll no: "))
gender=input("Gender: ")
marks=int(input("Enter the marks: "))

#create and object from a class
s=Student(name,gender,roll,marks)
s.display_details()
s.calculate_grade()
t=s.get_name_roll()
print(t[0])
print(t[1])

#define attributes for this Student object
"""
s=Student()
s.name=name
s.gender=gender
s.roll=roll
s.marks=marks
"""

#print the attributes of the object

"""print(s.gender)
print(s.roll)

s1=Student("asd","m",11,90)
s1.display_details()

print(s1.gender)
print(s1.marks)
"""

#student_ops.display_details(n,r,g)
#student_ops.calculategrade(m)
