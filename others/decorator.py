def outer_function(msg):
	def inner_function():
		print(msg)
	
	return inner_function

def decorator_function(original_function):
	def wrapper_function():
		print('before function call {}'.format(original_function.__name__))
		return original_function()
	return wrapper_function

def display():
	print('display is executed')

decorated_display = decorator_function(display)

decorated_display()

import time

def timer(function):
	def time_wrapper(*args, **kwargs):
		time_start = time.time()
		ret = function(*args, **kwargs)
		time_end = time.time()
		print('\nfunction: %r args:[%r, %r]\nellipse time: %f sec' % \
			(function.__name__, args, kwargs, time_end - time_start))
		return ret
	
	return time_wrapper

@timer
def loop(n=1000):
	for i in range(n):
		pass

loop()
