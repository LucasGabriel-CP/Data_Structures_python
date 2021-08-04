class Node():
    Data = int()
    def __init__(self, Val):
        self.Data = Val
        self.next = None
        self.prev = None

class ListDEOrd():
    def __init__(self):
        self.Head = None
        self.N = 0
    
    def push(self, Val):
        self.N += 1
        NewNode = Node(Val)
        AuxNode = self.Head

        if AuxNode is None:
            self.Head = NewNode
            return

        if AuxNode.Data > Val:
            NewNode.next = AuxNode
            NewNode.prev = AuxNode.prev
            self.Head = AuxNode.prev = NewNode
            return

        while AuxNode.next is not None and Val > AuxNode.next.Data:
            AuxNode = AuxNode.next
        NewNode.next = AuxNode.next
        NewNode.prev = AuxNode
        AuxNode.next = NewNode
        return

    def pop(self, Val):
        P = self.Head
        while P is not None and Val > P.Data:
            P = P.next
        if P is not None and P.Data is Val:
            if P.prev:
                (P.prev).next = P.next
            else:
                self.Head = P.next
            if P.prev:
                (P.next).prev = P.prev
            P = None
            self.N -= 1

    def Search(self, Val):
        P = self.Head
        while P is not None and Val > P.Data:
            P = P.next
        if P is not None and Val == P.Data:
            return True
        return False
    def isEmpty(self):
        return not self.N
    def printList(self):
        P = self.Head
        while P:
            print(P.Data)
            P = P.next

Lista = ListDEOrd()
Lista.push(4)
Lista.push(3)
Lista.push(6)
Lista.push(5)
Lista.pop(5)
Lista.printList()