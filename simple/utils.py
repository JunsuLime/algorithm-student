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
