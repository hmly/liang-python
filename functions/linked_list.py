# Ordered Linked List Class

class Node:
    def __init__(self, value):
        self.val = value
        self.next = None

    def getValue(self):
        return self.val

    def getNext(self):
        return self.next

    def setValue(self, value):
        self.val = value

    def setNext(self, next):
        self.next = next


class Linked_List:

    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None

    def add(self, item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp

    def size(self):
        current = self.head
        count = 0
        while current != None:
            count += 1
            current = current.getNext()
        return count

    def search(self, item):
        current = self.head
        found = False
        while current != None and not found:
            if current.getValue() == item:
                found = True
            else:
                current = current.getNext()
        return found

    def remove(self, item):
        current = self.head
        previous = None
        found = False
        while not found and current != None:
            if current.getValue() == item:
                found = True
            else:
                previous = current
                current = current.getNext()
        if current == None:
            return item + ' cannot be found'
        if previous == None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())

l = Linked_List()
print('is empty:', l.isEmpty())
l.add(50)
l.add('str')
l.add('346dd')
var = -1
l.add(var)
print('size:', l.size())
print('var found?:', l.search(var))
