class Thing():
    def __init__(self, Key, Val):
        self.key = Key
        self.val = Val
    def getKey(self):
        return self.key
    def getVal(self):
        return self.val

class Node(Thing):
    def __init__(self, Dat):
        self.Data = Thing(Dat.key, Dat.val)
        self.left = None
        self.right = None

def insert(R, key, Dat):
    if R is None:
        return Node(Dat)
    else:
        if key < (R.Data).getKey():
            R.left = insert(R.left, key, Dat)
        else:
            R.right = insert(R.right, key, Dat)
    return R

def delete(R, key):
    if not R:
        return R
    if key < (R.Data).getKey():
        R.left = delete(R.left, key)
        return R
    elif key > (R.Data).getKey():
        R.right = delete(R.right, key)
        return R
    
    if not R.left and not R.right:
        return None
    if not R.left:
        Aux = R.right
        R = None
        return Aux
    if not R.right:
        Aux = R.left
        R = None
        return Aux
    
    SucPai = R
    Sucesor = R.right
    while Sucesor:
        SucPai = Sucesor
        Sucesor = Sucesor.left
    if SucPai != R:
        SucPai.left = Sucesor.right
    else:
        SucPai.right = Sucesor.right

    R.Data(Sucesor.getKey(), Sucesor.getVal)
    return R

def inorder(P):
    if P is not None:
        inorder(P.left)
        print((P.Data).getKey(), (P.Data).getVal())
        inorder(P.right)

Coisa = Thing(50, 'a')
Root = None
Root = insert(Root, 50, Coisa)
Coisa = Thing(30, 'b')
Root = insert(Root, 30, Coisa)
Coisa = Thing(60, 'c')
Root = insert(Root, 60, Coisa)
inorder(Root)
print("######################")
delete(Root, 30)
inorder(Root)