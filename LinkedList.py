class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self, newData):
        self.data = newData

    def setNext(self, newNext):
        self.next = newNext

class LinkedList:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None

    def add(self, data):
        temp = Node(data)
        temp.setNext(self.head)
        self.head = temp

    def size(self):
        current = self.head
        count = 0
        while(current != None):
            count += 1
            current = current.getNext()
        return count

    def search(self, item):
        current = self.head
        found = False
        while(current is not None and not found):
            if current.data == item:
                found = True
            else:
                current = current.getNext()
        return found

    def remove(self, item):
        current = self.head
        previous = None
        found = False
        while(current is not None and not found):
            if current.data == item:
                found = True
            else:
                previous = current
                current = current.getNext()

        if previous is None and found:
            self.head = current.getNext()
        elif previous is not None and found:
            previous.setNext(current.getNext())
        else:
            raise AttributeError('cound not find the node')

    def clear(self):
        self.head = None
