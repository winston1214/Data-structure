# @Author YoungMinKim
# Data Structure - binary Tree Function - Postorder
class TNode:
    def __init__(self,data,left,right):
        self.data = data
        self.left = left
        self.right = right
def postorder(n): # 후위순회 LRV
    if n is not None:
        postorder(n.left)
        postorder(n.right)
        print(n.data,end='')

d=TNode('D',None,None)
e=TNode('E',None,None)
b=TNode('B',d,e)
f=TNode('F',None,None)
c=TNode('C',f,None)
root = TNode('A',b,c)

print('Post-order: ',end='')
postorder(root)