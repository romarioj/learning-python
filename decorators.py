# going to learn:
# 1. Functions inside functions
# 2. Returning functions
# 3. Functions as arguments

def hello(name='Jose'):
	print('the hello function has been run')

	def greet():
		return "	This is inside greet()"

	def welcome():
		return "	This is inside welcome()"

	if name == 'Jose':
		return greet
	else:
		return welcome

x = hello(name='Jose')
print(x()) # prints:
# the hello function has been run
#         This is inside greet()

y = hello(name = 'Sam')
print(y()) # prints:
# the hello function has been run
#         This is inside welcome()

print("\n")

def hello():
	return "Hi foo"

def other(func):
	print("some other code")
	# Assume that the func passed in is a function!!
	print(func())

other(hello)

def new_decorator(func):

	def wrap_func():
		print("some code before executing func")

		func()

		print("code here, after executing func()")

	return wrap_func

@new_decorator 
# this small line of code essentially it's this: #func_needs_decorator = new_decorator(func_needs_decorator)

def func_needs_decorator():
	print("Please, decorate me!!!")

func_needs_decorator() 
