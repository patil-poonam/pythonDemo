__author__='Poonam'
import re


def main():
	
	rule=re.compile(r'^\d{2}$')
	
	# \d{2} exact 2 digit ,
	# \d{4,5}4 or 5 digit acceptable ,  r=regular exp
	# $=end of rule set ,  ^ start of rule set
	
	input='22'
	print not rule.search(input)
	print '************************'
	print 'mobile no validation'

	rule1=re.compile(r'^(\+91)?[0]?[1789]\d{9}$')
	input1='8983546208'
	print not rule1.search(input1)
		# \+91 ..\ is use for string before +
		# ? is for OR
	
	print '*******************'
	print 'Email id Validation'
	email = 'poonampatil0710@gmail.com'
	print not re.match(r'^[A-Za-z0-9\._-]+\@[A-Za-z0-9]+\.[A-Za-z]+$',email)
	
if __name__=="__main__":
	main()
