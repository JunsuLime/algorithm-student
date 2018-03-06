class AbstractUnion(object):
	def union(self, e1, e2):
		raise NotImplementedError
	
	def connected(self, e1, e2):
		raise NotImplementedError

	def add(self):
		raise NotImplementedError

	def count(self):
		raise NotImplementedError

	def demo_init(self):
		raise NotImplementedError

	def display(self):
		raise NotImplementedError
	
class FUnion(AbstractUnion):
	def __init__(self):
		self.__gen_id = 0
		self.__connections = list()
	
	def union(self, e1, e2):
		cid1 = self.__connections[e1]
		cid2 = self.__connections[e2]

		for idx,cid in enumerate(self.__connections):
			if cid == cid2:
				self.__connections[idx] = cid1

	def connected(self, e1, e2):
		return self.__connections[e1] == self.__connections[e2]

	def add(self):
		self.__connections.append(self.__gen_id)
		self.__gen_id += 1

	def count(self):
		return len(self.__connections)

	def demo_init(self, n):
		for i in range(n):
			self.add()

	def display(self):
		print(self.__connections)

class UUnion(AbstractUnion):
	def __init__(self):
		self.__connections = list()

	def union(self, e1, e2):
		root1 = self.__find_root(e1)
		root2 = self.__find_root(e2)

		self.__connections[e2] = root1
	
	def connected(self, e1, e2):
		"""
		find roots of two elements.
		If roots are same, then e1 and e2 is connected
		"""
		root1 = self.__find_root(e1)
		root2 = self.__find_root(e2)

		return root1 == root2


	def __find_root(self, e):

		current_node = e
		while True:
			parent_node = self.__connections[current_node]

			if parent_node == current_node:
				return current_node

			current_node = parent_node


	def add(self):
		root_id = len(self.__connections)
		self.__connections.append(root_id)

	def count(self):
		return len(self.__connections)

	def display(self):
		print(self.__connections)

	def demo_init(self, n):
		for i in range(n):
			self.add()

class WeightedUUnion(AbstractUnion):
	def __init__(self):
		self.__connections = list()
		self.__sizes = list()

	def __find_root(self, e):

		while e != self.__connections[e]:
			parent = self.__connections[e]
			self.__connections[e] = self.__connections[parent]
			e = self.__connections[e]

		return e

	def union(self, e1, e2):
		root1 = self.__find_root(e1)
		root2 = self.__find_root(e2)

		if root1 == root2:
			return

		if self.__sizes[root1] < self.__sizes[root2]:
			self.__connections[root1] = root2
			self.__sizes[root2] += self.__sizes[root1]
		else:
			self.__connections[root2] = root1
			self.__sizes[root1] += self.__sizes[root2]
		pass

	def connected(self, e1, e2):
		root1 = self.__find_root(e1)
		root2 = self.__find_root(e2)

		return root1 == root2

	def add(self):
		root_id = len(self.__connections)
		self.__connections.append(root_id)
		self.__sizes.append(1)

	def demo_init(self, n):
		for i in range(n):
			self.add()

	def display(self):
		print(self.__connections)

	def count(self):
		return len(self.__connections)

if __name__ == "__main__":
	print("Hello world")
	uu = WeightedUUnion()
	uu.demo_init(6)

	uu.display()

	print(uu.connected(3,5))
	uu.union(1,2)
	uu.union(2,5)
	uu.union(5,3)
	print(uu.connected(3,5))

	uu.display()
	
	pass
