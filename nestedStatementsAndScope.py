# x = 'outside'

# def report():
# 	x = 'inside'
# 	return x

# print(report())
# print(x)

# # Scope - LEGB RULE
# # LOCAL
# def report():
# 	# LOCAL ASSIGNMENT!!
# 	x = 'local'
# 	print(x)

# ENCLOSING

# x = 'THIS IS GLOBAL LEVEL' # This is a global variable

# def enclosing():
# 	x = 'enclosing level' # This is an enclosing variable
# 	def inside():
# 		x = 'local' # This is a local variable
# 		print(x)
# 	inside()
# enclosing()

# GLOBAL
# BUILT-IN

x = 'outside'
def report(x):
	print(x)
	x = 'inside'
	return x

print(report(x))
print(x)
