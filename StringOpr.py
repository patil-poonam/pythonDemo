"""
Code for String Operations
"""
__author__= 'Poonam'

def StringOpr():

	a = raw_input("Enter the String");
	
	print a.capitalize()
	print a.count('a')
	print a.encode()
	print a.decode()
	print a.isalnum()
	print a.isdigit()
	
	print a.isalpha()
	print a.lower()

	print a.upper()

	print a.isspace()



if __name__== "__main__":
	StringOpr()

