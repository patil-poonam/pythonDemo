"""
This is First Code in python.
"""


__author__= 'Poonam'

def factorial():
	num = input("Please Enter Number: ")
	fact = 1
	for i in range(1,num+1):
		fact = fact * i
	print fact
	
if __name__== "__main__":
	factorial()
