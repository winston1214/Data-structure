# @Author YoungMinKim
# Data structure - queue
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
# 덱큐 -> 원형큐를 상속시켜서 구현
class CircularDeque(CircleQueue):
    def __init__(self):
        super().__init__()
    def addRear(self,item):self.enqueue(item)
    def deleteFront(self):
        return self.dequeue()
    def getFront(self):return self.peek()
    def addFront(self,item):
        if not self.isFull():
            self.items[self.front] = item
            self.front = self.front-1
            if self.front<0 : self.front = MAX_QSIZE-1
    def deleteRear(self):
        if not self.isEmpty():
            item = self.items[self.rear]
            self.rear = self.rear-1
            if self.rear<0:
                self.rear = MAX_QSIZE-1
                return item
    def getRear(self):
        return self.items[self.rear]

dq = CircularDeque()
for i in range(9):
    if i%2 == 0:dq.addRear(i)# 짝수는 후단에 삽입
    else:dq.addFront(i)
dq.display()
for i in range(2): dq.deleteFront()
for i in range(3): dq.deleteRear()
dq.display()
for i in range(9,14):dq.addFront(i)
dq.display()