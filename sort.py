"""
Code for Sorting Operations
"""
__author__= 'Poonam'

def StringOpr():

	a=[5,1,3,6,8]
	b=[5,1,3,6,8]
	c=[5,1,3,6,8]
	d=[5,1,3,6,8]
	i=0
	j=0
	
	for i in range(len(a)-1):
		for j in range(len(a)-(i+1)):
			if(a[j]<a[j+1]):
				temp=a[j]				
				a[j]=a[j+1]
				a[j+1]=temp
	print a


#--------------------------------------------------------------------
	b.sort(reverse=True)
	print b

#--------------------------------------------------------------------

	c.sort(cmp=lambda x,y : cmp(y,x))
	print c
#--------------------------------------------------------------------
	d.sort(cmp=lambda x,y :1 if x<y else -1)
	print d
#--------------------------------------------------------------------

if __name__== "__main__":
	StringOpr()

