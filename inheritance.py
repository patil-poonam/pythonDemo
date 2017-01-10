__author__='Poonam'
class Contact:
	all_contacts=[]
	def __init__(self,name):

		self.name=name
		self.all_contacts.append(name)



class Friend(Contact):

	def __init__(self,name):
		Contact.__init__(self,name) # can use super().__init__() in 3.x

def main():

	c=Contact('test')
	print c.all_contacts
	f=Friend('bjasd')
	print f.name
	print isinstance(f,Friend)
	
if __name__=='__main__':

	main()
