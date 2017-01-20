"""
This is a program for displaying the grade of student.
"""

__author__= 'Poonam'



sa= int(input("enter sub1 marks"))
sb= int(input("enter sub2 marks"))
sc= int(input("enter sub3 marks"))
sd= int(input("enter sub4 marks"))
se= int(input("enter sub5 marks"))

p= (sa+sb+sc+sd+se)/5

print("percentage of student are:",p)

if(p<40):
	print("the student is FAIL")
elif(p>75):
	print("the student has DISTINCTION")
elif(p>60):
	print("the student has FIRST CLASS")
elif(p>40):
	print("the student is PASS")
