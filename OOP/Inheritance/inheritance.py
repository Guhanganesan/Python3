# Python code to demonstrate how parent constructors
# are called.

# parent class
class College:

	# __init__ is known as the constructor
	def __init__(self, name, idnumber):
		self.name = name
		self.idnumber = idnumber
		
	def details(self):
		print("My name is {}".format(self.name))
		print("IdNumber: {}".format(self.idnumber))
	
# child class
class Student(College):
	def __init__(self, name, idnumber, fees, section):
		self.fees = fees
		self.section = section

		# invoking the __init__ of the parent class
		College.__init__(self, name, idnumber)
		#super().details()
		
	def details(self):
		print("My name is {}".format(self.name))
		print("IdNumber: {}".format(self.idnumber))
		print("Post: {}".format(self.section))


# creation of an object variable or an instance
a = Student('Rahul', 886012, 200000, "A")

# calling a function of the class Person using
# its instance
a.details()