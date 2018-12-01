#TODO: add delete function
from queue import Queue
from stack import Stack

class Node:
	def __init__(self,data):
		self._data = data
		self._left = None
		self._right = None
		self._parent = None

	@property
	def data(self):
		return self._data

	@property
	def left(self):
		return self._left

	@left.setter
	def left(self, value):
		self._left = value

	@left.deleter
	def left(self):
		self._left = None

	@property
	def right(self):
		return self._right

	@right.setter
	def right(self, value):
		self._right = value

	@right.deleter
	def right(self):
		self._right = None

	@property
	def parent(self):
		return self._parent

	@parent.setter
	def parent(self, value):
		self._parent = value

	@parent.deleter
	def parent(self):
		self._parent = None

class BinaryTree:
	def __init__(self):
		self._root = None

	@property
	def root(self):
		return self._root

	@root.setter
	def root(self, value):
		self._root = value

	@root.deleter
	def root(self):
		self._root = None

	def add(self, item):
		node = Node(item)
		if(self.root is None):
			self.root = node
		else:
			current = self.root
			while(current is not None):
				if(current.data > node.data):
					previous = current
					current = current.left
				else:
					previous = current
					current = current.right

			if(previous.data > node.data):
				previous.left = node
			else:
				previous.right = node
			node.parent = previous

	def search(self, value):
		current = self.root
		while(current is not None):
			if(current.data > value):
				current = current.left
			elif(current.data < value):
				current = current.right
			else:
				return current
		return None

	def delete(self, item):
		node = self.search(item)
		if(node is not None):
			if(self._leaf(node)):
				if(self._isRightChildren(node)):
					del node.parent.right
					del node
				else:
					del node.parent.left
					del node

			elif(node.left is not None and node.right is None):
				if(self._isRightChildren(node)):
					node.parent.right = node.left
					node.left.parent = node.parent
				else:
					node.parent.left = node.left
					node.left.parent = node.parent
				del node

			elif(node.left is None and node.right is not None):
				if(self._isRightChildren(node)):
					node.parent.right = node.right
					node.right.parent = node.parent
				else:
					node.parent.left = node.right
					node.right.parent = node.parent
				del node
				
			elif(node.left is not None and node.right is not None):
				rmin = self.min(node.right)
				if(rmin != node.right):
					rmin.right = node.right
					del rmin.parent.left

				rmin.left = node.left
				rmin.parent = node.parent
				node.left.parent = rmin
				if(self._isRightChildren(node)):
					node.parent.right = rmin
				else:
					node.parent.left = rmin
				del node

	def _isRightChildren(self, node):
		if(node == node.parent.right):
			return True
		return False

	def empty(self):
		return True if self.root is None else False

	def _leaf(self, node):
		if(node.left is None and node.right is None):
			return True
		return False

	def max(self, root):
		while(root.right is not None):
			root = root.right
		return root

	def min(self, root):
		while(root.left is not None):
			root = root.left
		return root

	def preorder(self, root):
		if(root is None):
			return
		print(root.data, end=' ')
		self.preorder(root.left)
		self.preorder(root.right)


	def postorder(self, root):
		if(root is None):
			return
		self.postorder(root.left)
		self.postorder(root.right)
		print(root.data, end=' ')

	def inorder(self, root):
		if(root is None):
			return
		self.inorder(root.left)
		print(root.data, end=' ')
		self.inorder(root.right)

	def queuelevelorder(self, root):
		if(root is None):
			return

		q = Queue()
		q.put(root)
		while(not q.isEmpty()):
			temp = q.get()
			print(temp.data, end=' ')

			if(temp.left is not None):
				q.put(temp.left)

			if(temp.right is not None):
				q.put(temp.right)

'''
					50
				  /	  \
				 45	    60
				/  \    / \
			   40  46  55  70
			  /		  / \   \
			 30		 54  56  80
			/ \		 /	  \    \
		   15 35    53	   57   90
		  /   / \
		 14  34 36

'''






if __name__ == '__main__':
	pass
