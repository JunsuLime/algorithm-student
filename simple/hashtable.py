class HashTable(object):
	def __init__(self, n=8):
		self.__container = [list() for _ in range(n)]

	def get(self, key):
		hash_key = self.__hash_func(key)
		h_list = self.__container[hash_key]
		for k, v in h_list:
			if k == key:
				return v
		return None

	def put(self, key, value):
		hash_key = self.__hash_func(key)
		h_list = self.__container[hash_key]

		for i in range(len(h_list)):
			k, v = h_list[i]
			if k == key:
				h_list[i] = (key, value)
				return

		h_list.append((key, value))
		

	def __hash_func(self, key):
		return key % len(self.__container)

	
	def __repr__(self):
		return str(self.__container)
	

if __name__ == '__main__':
	hashtable = HashTable()
	hashtable.put(3, 15)
	hashtable.put(35, 16)
	print(hashtable.get(3))
	print(hashtable.get(35))
	print(hashtable)
