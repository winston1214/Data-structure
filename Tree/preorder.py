# @Author YoungMinKim
# Data Structure - binary Tree Function - Preorder
class TNode:
    def __init__(self,data,left,right):
        self.data = data
        self.left = left
        self.right = right
def preorder(n): # 전위순회 VLR
    if n is not None:
        print(n.data,end='')
        preorder(n.left)
        preorder(n.right)

d=TNode('D',None,None)
e=TNode('E',None,None)
b=TNode('B',d,e)
f=TNode('F',None,None)
c=TNode('C',f,None)
root = TNode('A',b,c)

print('Pre-order: ',end='')
preorder(root)