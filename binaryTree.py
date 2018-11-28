#TODO: add delete function
from queue import Queue
from stack import Stack

class Node:
	def __init__(self,data):
		self.data = data
		self.left = None
		self.right = None
		self.parent = None

	def getData(self):
		return self.data

	def getLeft(self):
		return self.left

	def getRight(self):
		return self.right

	def getParent(self):
		return self.parent

	def setLeft(self, value):
		self.left = value

	def setRight(self, value):
		self.right = value

	def setParent(self, value):
		self.parent = value

class BinaryTree:
	def __init__(self):
		self.root = None

	def add(self, item):
		temp = Node(item)
		if self.root == None:
			self.root = temp
		else:
			previous = self.root
			if self.root.getData() > temp.getData():
				current = self.root.getLeft()
			else:
				current = self.root.getRight()
			while(current is not None):
				if current.getData() > temp.getData():
					previous = current
					current = current.getLeft()
				else:
					previous = current
					current = current.getRight()
			if previous.getData() > temp.getData():
				previous.setLeft(temp)
			else:
				previous.setRight(temp)
			temp.setParent(previous)

	def search(self, value):
		previous = self.root
		if self.root.getData() > value:
			current = self.root.getLeft()
		elif self.root.getData() < value:
			current = self.root.getRight()
		else:
			return True
		while(current is not None):
			if current.getData() > value:
				previous = current
				current = current.getLeft()
			elif current.getData() < value:
				previous = current
				current = current.getRight()
			else:
				return True
		return False

	def getRoot(self):
		return self.root


	def __isRightChildren(self, node):
		if(node == node.getParent().getRight()):
			return True
		return False

	def __isLeftChildren(self, node):
		if(node == node.getParent().getLeft()):
			return True
		return False

	def getMax(self, root):
		if(root.getRight() is not None):
			self.getMax(root.getRight())
		else:
			print(root.getData())
			return

	def getMin(self, root):
		if(root.getLeft() is not None):
			self.getMin(root.getLeft())
		else:
			print(root.getData())
			return

	def queuelevelorder(self, root):
		if(root is None):
			return

		q = Queue()
		q.put(root)
		while(not q.isEmpty()):
			temp = q.get()
			print(temp.getData(), end=' ')

			if(temp.getLeft() is not None):
				q.put(temp.getLeft())

			if(temp.getRight() is not None):
				q.put(temp.getRight())

	def preorderRecursive(self, root):
		if(root is None):
			return
		print(root.getData(), end=' ')
		self.preorderPrint(root.getLeft())
		self.preorderPrint(root.getRight())


	def postorderRecursive(self, root):
		if(root is None):
			return
		self.preorderPrint(root.getLeft())
		self.preorderPrint(root.getRight())
		print(root.getData(), end=' ')

	def inorderRecursive(self, root):
		if(root is None):
			return
		self.preorderPrint(root.getLeft())
		print(root.getData(), end=' ')
		self.preorderPrint(root.getRight())

	def reverseInorderRecursive(self, root):
		if(root is None):
			return
		self.preorderPrint(root.getRight())
		print(root.getData(), end=' ')
		self.preorderPrint(root.getLeft())

	def StackPreorder(self, root):
		if(root is None):
			return
		s = Stack()
		s.push(root)
		while(s.isEmpty() is False):
			temp = s.pop()
			print(temp.getData(), end=' ')

			if(temp.getRight()):
				s.push(temp.getRight())
			if(temp.getLeft()):
				s.push(temp.getLeft())








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
	x.getMax(x.getRoot())
	x.getMin(x.getRoot())
	x.StackPreorder(x.getRoot())
	#print(x.getMin().getData())
