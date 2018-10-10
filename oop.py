# Object Oriented Programming

mylist = [1,2,3]
mylist.append(4)
print(type(mylist)) # Everything in python is an object, and you
# can check that by using the type() keyword. 
# it will print out what type of object it is: <class 'list'>
print(type(23.5)) # <class 'float'>

# Let's create our own class
class Sample():
	pass # class is totally empty it doesn't do anything

x = Sample()

print(type(x)) # prints out <class '__main__.Sample'>
# BAAM WE CRATED OUR OWN OBJECT TYPE, in this case it happens to be
# a simple class named Sample

# let's create a new class
class Dog():
	def __init__(self, input_breed): # "self" represents the instance of the class. It binds the attributes with the given arguments.
		self.breed = input_breed 
	# By concention, the input parameter shares the name of the input attribute
	# Such as:
	# def __init__(self,breed):
	# 	self.breed = breed

x = Dog('Husky') # self, essentially becomes x here
print(type(x)) # <class '__main__.Dog'>
print(type(x.breed)) # <class 'str'>
print(x.breed) # Husky

# HERE'S AN EXAMPLE:
class Dog():

	# CLASS OBJECT ATTRIBUTES: things that are ALWAYS going to be true, regardless of the instance of the DOG
	species = 'mammal'
	# In this case, you can change the breed of the dog, the name, or whatever
	# Either way, the dog's species is always going to be a mammal

	def __init__(self,breed,name):
		self.breed = breed
		self.name = name

lilly = Dog('Golden Retreiver','Lilly')
new_dog = Dog('German Shepard', 'Rudger')

print(lilly.breed)
print(lilly.name)
print(lilly.species)
print(new_dog.name)
print(new_dog.species)

# DEFINITION TIME:
# Class is a set or category of things having some property or attribute in common and differentiated from others by kind, type, or quality.
# object is one of instances of the class. which can perform the functionalities which are defined in the class.
# self: self represents the instance of the class. By using the "self" keyword we can access the attributes and methods of the class in python.
# "__init__" is a reseved method in python classes. It is known as a constructor in object oriented concepts. This method called when an object is created from the class and it allow the class to initialize the attributes of a class.
#  "self"  represents the instance of the class. It binds the attributes with the given arguments.

class Rectangle:
	def __init__(self,length,width,unit_cost=0):
		self.length = length
		self.width = width
		self.unit_cost = unit_cost # usd/m^2

	def perimeter(self):
		return 2 * (self.length + self.width)

	def area(self):
		return self.length * self.width

	def cost(self):
		area = self.area()
		return area * self.unit_cost # m^2 * usd/m^2 = usd

# width = 1.20 m, length 1.6 m, 1c^2 = Rs 3
r = Rectangle(1.6,1.2,3)
print("\nThe perimeter is: %s m" % (r.perimeter()))
print("Area of Rectangle: %s m^2" % (r.area()))
print("Cost of rectangular field: Rs. %s \n" % (r.cost()))



class Circle():

	pi = 3.14

	def __init__(self,radius=1): # self-assign radius = 1 if the user does not specify it
		self.radius = radius

	def area(self):
		return self.pi * self.radius * self.radius

	def circumference(self):
		return 2 * self.pi * self.radius

myCircle = Circle(10)
print(myCircle.radius)
print("The area is %s units^2" % (myCircle.area()))
print("The circumference is %s units\n" % (round(myCircle.circumference(),2)))

class Animal(): # base class

	def __init__(self):
		print('Animal created!')

	def report(self):
		print('Animal')

	def eat(self):
		print('Eating!')

a = Animal()
a.eat()
a.report()

class Doge(Animal): # derived class
# Here we're able to use the methods crated on the previous class
# And we use these methods in this new class without having to create new methods such as eat or report. 

	def __init__(self):
		Animal.__init__(self)
		print('Dog Created!')

	def report(self):
		print('I am a doge') # Rewrites the report(self) specifically for the inheritance method under Doge()

d = Doge()
d.eat()
d.report()

# METHODs: functions defined inside the body of a class and they're used to 
# perform operations with the attributes with the objects of our classes


# SPECIAL METHODS

class Book():
	def __init__(self,title,author,pages):
		self.title = title
		self.author = author
		self.pages = pages

	def __repr__(self): # string representation of an object
		return f"\nTitle: {self.title} \nAuthor: {self.author} \nPages: {self.pages}"
		# this can be done with __str__ but Flask uses __repr__

	def __len__(self): # length of an object
		return self.pages

mybook = Book("Python Rocks!", 'Dan The Man', 250)
print(mybook) # prints out __repr__

length_book = len(mybook) # prints out __len__, length
print(length_book) # prints out 250, length of book