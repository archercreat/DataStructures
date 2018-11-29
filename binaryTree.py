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

	@property
	def right(self):
		return self._right

	@right.setter
	def right(self, value):
		self._right = value

	@property
	def parent(self):
		return self._parent

	@parent.setter
	def parent(self, value):
		self._parent = value

class BinaryTree:
	def __init__(self):
		self._root = None

	@property
	def root(self):
		return self._root

	@root.setter
	def root(self, value):
		self._root = value

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
		return False

	def delete(self, item):
		pass

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

'''
					50
				  /	  \
				 45	    60
				/  \    / \
			   40  46  55  70
			  /		  / \   \
			 30		 54  56  80
			/ \		 /	  \    \
		   15 30    53	   57   90
		  /
		 14

'''






if __name__ == '__main__':

	x = BinaryTree()
	x.add(50)
	x.add(45)
	x.add(46)
	x.add(40)
	x.add(30)
	x.add(30)
	x.add(60)
	x.add(70)
	x.add(15)
	x.add(14)
	x.add(55)
	x.add(54)
	x.add(56)
	x.add(53)
	x.add(57)
	x.add(80)
	x.add(90)
	print('inorder')
	x.inorder(x.root)
	print('\npreorder')
	x.preorder(x.root)
	print('\npostorder')
	x.postorder(x.root)
	print('\n')
