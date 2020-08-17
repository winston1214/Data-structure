# @Author YoungMinKim
# Data structure - Queue
# 원형큐
MAX_QSIZE = 10
class CircleQueue: # 원형으로 움직이는 큐
    
    def __init__(self):
        self.front=0
        self.rear=0
        self.items = [None]*MAX_QSIZE
    def isEmpty(self):
        return self.front == self.rear
    def isFull(self):
        return self.front == (self.rear+1) % MAX_QSIZE # f
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

q = CircleQueue()
for i in range(8):
    q.enqueue(i)
q.display()
for i in range(5):
    q.dequeue()
q.display()
for i in range(8,14):
    q.enqueue(i)
q.display()