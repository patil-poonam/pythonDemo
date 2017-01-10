__author__='Poonam'

class Person:

	Title=('Dr','Ms','Mr','Mrs')


	def __init__(self,name,surname):

		self.name=name
		self.surname=surname

	def fullname(self):
		return "%s %s" % (self.name,self.surname)


	@classmethod
	def allowed_title_starting_with(self,startswith):
		return [t for t in self.Title if t.startswith(startswith)]

	@staticmethod

	def allowed_tite_ending_with(endswith):

		return [t for t in Person.Title if t.endswith(endswith)]

def main():

		jane = Person("Poonam","Patil")

		print jane.fullname()
		print (jane.allowed_title_starting_with("M"))
		print (Person.allowed_title_starting_with("M"))

		print (jane.allowed_tite_ending_with("s"))
		print (Person.allowed_tite_ending_with("s"))
if __name__== '__main__':
	main()
