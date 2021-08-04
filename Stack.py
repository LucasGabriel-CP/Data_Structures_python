class Node():
    Data = int()
    def __init__(self, Val):
        self.Data = Val
        self.next = None

class stack():
    def __init__(self):
        self.Top = None
        self.N = 0
    
    def push(self, Val):
        self.N += 1
        NewNode = Node(Val)
        NewNode.next = self.Top
        self.Top = NewNode
        return
    def pop(self):
        if self.N == 0:
            return
        self.N -= 1
        P = self.Top
        self.Top = P.next
        P = None
    
    def top(self):
        if self.Top:
            return self.Top
        return -1

    def isEmpty(self):
        return not self.N
    def printstack(self):
        P = self.Top
        while P:
            print(P.Data)
            P = P.next

Pilha = stack()
Pilha.push(4)
Pilha.push(3)
Pilha.push(6)
Pilha.push(5)
Pilha.printstack()
Pilha.pop()
Pilha.printstack()