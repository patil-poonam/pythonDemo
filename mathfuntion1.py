"""
This is a program for demonstration of various list methods.
"""

__author__= 'Poonam'

import math
n = int (input("Enter number"))
print ("Number is: ",n)

a = abs(n)    #
print('Absolute of number is:',a)

s= math.sqrt(n)
print ('Square root of number is:',s)


l= math.log(n)
print ("Logarithm is:",l)

lo= math.log10(n)
print ("Base 10 Logarithm is:",lo)

e = math.exp(n)
print ("The exponential is: ",e)

c = math.ceil(n)
print ("The ceiling is: ",c)

y = int (input("Enter power"))
print ("power is: ",y)

p = math.pow(n,y)
print ('The value of power',p)



