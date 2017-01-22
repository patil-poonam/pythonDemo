"""
This is a program for demonstration of various dictionary methods.
"""

__author__= 'Poonam'

dict1 = {'Name':'Sushant','Age':26,'Branch':'Computer'}

dict2 = {'Name':'Prashant','Age':22,'Branch':'Chemical'}

print (dict1)
print (dict2)

l = len(dict1)                          #calculate length of string
print ("Length of dictionary is:",l)

str1 = str(dict1)                       #produces printable string
print ('printable string is:',str1)

print ("Variable type:", type(dict1))    #return type of the passed variable

print ("Dict items %s" %(dict1.items()))   #returns dicts tuple pair

print ("Dict keys %s" %(dict1.keys()))    #returns list of all available keys

print ("Dict values %s" %(dict1.values()))  #returns list of all available values 
