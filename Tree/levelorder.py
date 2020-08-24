# @Author YoungMinKim
# Data Structure - binary Tree Function - LevelOrder

MAX_QSIZE = 10
class CircleQueue: # 원형큐
    
    def __init__(self):
        self.front=0
        self.rear=0
        self.items = [None]*MAX_QSIZE
    def isEmpty(self):
        return self.front == self.rear
    def isFull(self):
        return self.front == (self.rear+1) % MAX_QSIZE # full
    def clear(self):
        self.front = self.rear
    def enqueue(self,item): # 삽입함수
        if not self.isFull():
            self.rear = (self.rear+1)%MAX_QSIZE # rear 회전
            self.items[self.rear] = item # rear 위치에 삽입
    def dequeue(self): # 삭제
        if not self.isEmpty(): # front 회전
            self.front = (self.front+1) % MAX_QSIZE # front 위치의 항목 반환
            return self.items[self.front]
    def peek(self): # 삭제하지 않고 반환
        if not self.isEmpty():
            return self.items[(self.front+1)%MAX_QSIZE] 
    def size(self):
        return (self.rear - self.front + MAX_QSIZE) % MAX_QSIZE
    def display(self):
        out = []
        if self.front<self.rear:
            out = self.items[self.front+1:self.rear+1]
        else:
            out = self.items[self.front+1:MAX_QSIZE] + self.items[0:self.rear+1]
        print('f={},r={}'.format(self.front,self.rear),out)
class TNode:
    def __init__(self,data,left,right):
        self.data = data
        self.left = left
        self.right = right
def levelorder(root): # 레벨순회 - 원형큐로 구현
    queue = CircleQueue()
    queue.enqueue(root)
    while not queue.isEmpty(): # 큐가 공백상태가 아닌 동안
        n = queue.dequeue() # 큐에서 맨 앞의 노드 n을 꺼낸다
        if n is not None:
            print(n.data,end='')
            queue.enqueue(n.left)
            queue.enqueue(n.right)

d=TNode('D',None,None)
e=TNode('E',None,None)
b=TNode('B',d,e)
f=TNode('F',None,None)
c=TNode('C',f,None)
root = TNode('A',b,c)

print('Level-order: ',end='')
levelorder(root)
