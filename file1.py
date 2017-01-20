"""
This is a program for countig the number of lines,blank spaces,comment lines and tabs in file.
"""

__author__= 'Poonam'


fd = open("abc.txt")
i = 0
spaces = 0
tabs = 0
comm = 0
cnt = 0

for i,line in enumerate(fd):
    spaces += line.count(' ')
    tabs += line.count('\t')
    comm += line.count('#')
fd.close()

print "spaces :",spaces
print "tabs : ",tabs
print "number of line :",i + 1
print "number of comment lines: ",comm


