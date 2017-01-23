"""
This is a program for demonstration of nested if INCOME TAX CALCULATOR.
"""

__author__= 'Poonam'

income= int(input("enter Income of Person\n"))

p= input("enter char M if MALE and F if FEMALE\n")

if(p=='M'):
	if(income<150000):
		print("Male income tax payable is: 0")
	elif(income>150000):
		print("MAle income tax payable is:",(income/10))
else:
	if(income<200000):
		print(" Female income tax payable is: 0")
	elif(income>200000):
		print("Female income tax payable is:",(income/10))
