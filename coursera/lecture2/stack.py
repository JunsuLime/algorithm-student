class AbstractStack(object):
	def push(self, e):
		raise NotImplementedError
	
	def pop(self):
		raise NotImplementedError

	def is_empty(self):
		raise NotImplementedError

class Stack(AbstractStack):
	def __init__(self):
		self.__container = list()

	
	def push(self, e):
		self.__container.append(e)

	def pop(self):
		self.__container.pop()

	def is_empty(self):
		return len(self.__container) == 0
	
	def __len__(self):
		return len(self.__container)

class LinkedList(object):



	class Node(object):
		def __init__(self, e, n=None):
			self.next = n
			self.element = e


class StackWithMax(AbstractStack):
	"""
	implement stack that have max method
	"""
	
	pass


if __name__ == "__main__":
	pass
