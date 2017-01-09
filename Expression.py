"""
Code for a^n + b^n = c^n evaluation in python.
"""
__author__= 'Poonam'

def exp_function():

	a = input("Please Enter a's Value: ")
	b = input("Please Enter b's Value: ")
	c = input("Please Enter c's Value: ")
	n = input("Please Enter n's Value: ")
	
	if a**n + b**n == c**n:
		print 'Equal'
	else :
		print 'Not Equal'

if __name__== "__main__":
	exp_function()

