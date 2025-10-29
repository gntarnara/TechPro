class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def addElement(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def length(self):
        counter = 1
        current = self.head
        if current == None:
            return 0

        while current.next != None:
            current = current.next
            counter += 1
        return counter

    def printEverything(self):
        current = self.head
        if current == None:
            print("This list hasnt got any data")
        else:
            while current != None:
                print(current.data)
                current = current.next

    def get(self, n):

        current = self.head

        if n >= self.length():
            print("You are out of Limits")
        else:
            for i in range(n):
                current = current.next
            print(current.data)


L = LinkedList()
L.addElement("N")
L.addElement("Y")


print(L.head.data)
print(L.length())
L.printEverything()
L.get(0)
