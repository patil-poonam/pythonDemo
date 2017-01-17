"""
This is Code for dictionary demo.
"""


__author__= 'Poonam'

def avg():
	temp=0	
	students=[{'name':'xyz','marks':64},{'name':'pqr','marks':65},{'name':'abc','marks':84}]
	
	for i in students: 
		temp = temp+ i['marks']	
		print i['name'] ,i['marks']	
	print "-------"	
	print "avg", temp / len(students)


if __name__== "__main__":
	avg()
