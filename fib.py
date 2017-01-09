

___author___='Vishwesh'



def fib (n): 
	if( n == 0):
    		return 0
	else:
		x = 0 
    	y = 1 
    	for i in range(1,n):
      		y =y+x
       		x=y
    	return y

ls=[]
number=input("Enter the range")	
for i in range(number):
	ls.append((fib(i)))

print ls

for i in range(len(ls)):
	ls[i] =ls[i]**3     # For printing their cube also

print ls
if __name__== "__main__":
	fib(i)
