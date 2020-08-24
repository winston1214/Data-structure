# @Author YoungMinKim
# Data Structure - binary Tree Function - count_node,count_leaf,calculater height
class TNode:
    def __init__(self,data,left,right):
        self.data = data
        self.left = left
        self.right = right
def count_node(n): # 노드의 개수 세기
    if n is None:
        return 0
    else:
        return 1+count_node(n.left) + count_node(n.right) # 좌우 트리 합 + 1(루트)
def count_leaf(n): # 단말 노드 개수 세기
    if n is None: # 공백트리
        return 0
    elif n.left is None and n.right is None: # 단말노드 --> 1
        return 1
    else:
        return count_leaf(n.left)+count_leaf(n.right) # 좌우 서브트리의 결과 합 반환
def calc_height(n): # 트리 높이 구하기
    if n is None:
        return 0
    hLeft = calc_height(n.left)
    hRight = calc_height(n.right)
    if hLeft>hRight:
        return hLeft+1
    else:
        return hRight+1

d=TNode('D',None,None)
e=TNode('E',None,None)
b=TNode('B',d,e)
f=TNode('F',None,None)
c=TNode('C',f,None)
root = TNode('A',b,c)

print('노드의 개수 : {}'.format(count_node(root)))
print('단말의 개수 : {}'.format(count_leaf(root)))
print('트리의 높이 : {}'.format(calc_height(root)))

