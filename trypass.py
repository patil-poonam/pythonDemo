"""
This is Python Code for exception handling using try,except,else and finally block.
"""


__author__= 'Poonam'



def divide(x,y):
	try: 
		result=x/y
	except Exception, e:
		print 'Exception is ',e
	else :
		print 'result is',result
	finally:
		print 'executing final block'
	print '--------------------------------'
def factorial():
	divide(20,1)
	divide(20,0)

if __name__== "__main__":
	factorial()

