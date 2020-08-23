# Python code to illustrate 
# Decorators with parameters in Python 
# https://www.geeksforgeeks.org/decorators-with-parameters-in-python/


def decorator_func(x, y): 

	def Inner(func): 

		def wrapper(*args, **kwargs): 
			print("I like Geeksforgeeks") 
			print("Summation of values - {}".format(x+y) ) 

			func(*args, **kwargs) 
			
		return wrapper 
	return Inner 


# Not using decorator 
def my_fun(*args): 
	for ele in args: 
		print(ele) 

# another way of using dacorators 
decorator_func(12, 15)(my_fun)('Geeks', 'for', 'Geeks') 
