"""
This is a program for demonstration of various list methods.
"""

__author__= 'Poonam'

list1= ['computr', 1991, 60]
list2 = ['Mechanical',1987,120]
list3 = [10,12,10,15]

print (list1)
print (list2)
print (list3)

list1.append('SSBT')
print (list1)

a= list3.count(10)
print ('Times occurs:',a)

list1.extend(list2)
print ('Extended list is:',list1)

list3.insert(2,50)
print ('list after append:',list3)

list3.reverse()
print('Reverse list is:',list3)





