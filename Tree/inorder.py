# @Author YoungMinKim
# Data Structure - binary Tree Function - Inorder
class TNode:
    def __init__(self,data,left,right):
        self.data = data
        self.left = left
        self.right = right
def inorder(n): # 중위순회 LVR
    if n is not None:
        inorder(n.left)
        print(n.data,end='')
        inorder(n.right)

d=TNode('D',None,None)
e=TNode('E',None,None)
b=TNode('B',d,e)
f=TNode('F',None,None)
c=TNode('C',f,None)
root = TNode('A',b,c)

print('In-order: ',end='')
inorder(root)