class DoubleLinkedList(object):
	class Node(object):
		def __init__(self, e):
			self.__item = e
			self.__next = None
			self.__prev = None


		def set_next(self, n):
			self.__next = n

		def get_next(self):
			return self.__next

		def set_prev(self, p):
			self.__prev = p

		def get_prev(self):
			return self.__prev

		def get_item(self):
			return self.__item
		
		def __repr__(self):
			return str(self.__item)

	def __init__(self, l=None):
		self.__head = None
		if l:
			for e in l:
				self.append(e)


	def first_node(self):
		return self.__head
	
	def append(self, e):
		n = DoubleLinkedList.Node(e)
		if not self.__head:
			self.__head = n
			n.set_next(n)
			n.set_prev(n)
		else:
			current = self.__head
			prev = self.__head.get_prev()

			prev.set_next(n)
			current.set_prev(n)
			n.set_next(current)
			n.set_prev(prev)
	
	def stride(self, node, stride):
		for _ in range(stride):
			node = node.get_next()

		return node

	def delete_node(self, node):
		if node.get_next() == self.__head and node.get_prev() == self.__head:
			self.__head = None
			return None
		else:
			prev_n = node.get_prev()
			next_n = node.get_next()

			prev_n.set_next(next_n)
			next_n.set_prev(prev_n)

			if node == self.__head:
				self.__head = next_n
			return next_n

	
	def __repr__(self):
		if not self.__head:
			return str([])
		else:
			l = list()
			l.append(self.__head.get_item())

			current = self.__head.get_next()
			while current != self.__head:
				l.append(current.get_item())
				current = current.get_next()
			return str(l)
		

n, stride = map(int, input().split())

# adjust real jump value
stride = stride - 1

l = DoubleLinkedList(list(range(1, n+1)))
# print(l)

node = l.first_node()
# print("current node: %r" % node)

delete_order_list = list()

while node:
	node = l.stride(node, stride)
	delete_order_list.append(node.get_item())
	node = l.delete_node(node)

delete_order_list = str(delete_order_list)
print(delete_order_list.replace('[', '<').replace(']', '>'))
