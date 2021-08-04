class Node():
    Data = int()
    def __init__(self, Val):
        self.Data = Val
        self.next = None

class queue():
    def __init__(self):
        self.Head = None
        self.Tail = None
        self.N = 0
    
    def push(self, Val):
        self.N += 1
        NewNode = Node(Val)
        if self.Head:
            self.Tail.next = NewNode
        else:
            self.Head = NewNode
        self.Tail = NewNode
        NewNode.next = None
        return
    def pop(self):
        if self.N == 0:
            return
        self.N -= 1
        P = self.Head
        self.Head = P.next
        P = None
        if not self.Head:
            self.Tail = None

    def front(self):
        if self.Head:
            return (self.Head).Data
        return -1
    def back(self):
        if self.Head:
            return (self.Tail).Data
        return -1

    def isEmpty(self):
        return not self.N
    def printQueue(self):
        P = self.Head
        while P:
            print(P.Data)
            P = P.next

Fila = queue()
Fila.push(4)
Fila.push(3)
Fila.push(6)
Fila.push(5)
Fila.printQueue()
Fila.pop()
Fila.printQueue()