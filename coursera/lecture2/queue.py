class AbstactQueue(object):
	pass


class QueueByStack(AbstractQueue):
	"""
	implement queue composed by stack

	hint - two stack
	"""
	pass

class Queue(object):
	"""
	python list is internally implemented by array with auto-resize
	
	TODO: complete this ...
	"""

	def __init__(self):
		self.__container = list()
		self.__head = 0
		self.__tail = 0

	def enqueue(self, e):
		self.__container.append(e):
		self.__tail += 1
	
	def dequeue(self):
		self.__head
