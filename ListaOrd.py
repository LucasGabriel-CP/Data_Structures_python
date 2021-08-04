class Node():
    Data = int()
    def __init__(self, Val):
        self.Data = Val
        self.next = None
class ListOrd():
    def __init__(self):
        self.Head = None
        self.It = None
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
            self.Head = NewNode
            return

        while AuxNode.next is not None and Val > AuxNode.next.Data:
            AuxNode = AuxNode.next
        NewNode.next = AuxNode.next
        AuxNode.next = NewNode
        if self.N == 1:
            self.It = NewNode
        return

    def pop(self, Val):
        P = self.Head
        if P is not None and Val is P.Data:
            self.Head = P.next
            P = None
            return
        AuxNode = None
        while P is not None and Val > P.Data:
            AuxNode = P
            P = P.next
        if P is not None and P.Data is Val:
            AuxNode.next = P.next
            if self.It is AuxNode:
                self.It = P
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

Lista = ListOrd()
Lista.push(4)
Lista.push(3)
Lista.push(6)
Lista.push(5)
Lista.pop(5)
print(Lista.isEmpty())