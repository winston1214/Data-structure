# @Author YoungMinKim
# baekjoon

# 우선순위 큐 -> 힙트리 이용 X
class PriorityQueue:
    def __init__(self):
        self.items=[]
    def isEmpty(self):
        return len(self.items) == 0
    def size(self): return len(self.items)
    def clear(self) : self.items=[]
    def enqueue(self,item):
        self.items.append(item) # list 맨 뒤에 삽입
    def findMaxIndex(self): # 최대 우선순위 항목의 인덱스 반환
        if self.isEmpty():return None
        else:
            highest = 0 # 일단 0을 최대라 하고
            for i in range(1,self.size()): # 모든 항목에 대해
                if self.items[i]>self.items[highest]:
                    highest = i # 최고 우선순위 인덱스 갱신
        return highest
    def dequeue(self): # 삭제
        highest = self.findMaxIndex() # 우선순위가 가장 높은 항목 삭제
        if highest is not None:
            return self.items.pop(highest)
    def peek(self): # 삭제하지 않고 그냥 반환
        highest = self.findMaxIndex()
        if highest is not None:
            return self.items[highest]
q= PriorityQueue()
q.enqueue(34)
q.enqueue(18)
q.enqueue(27)
q.enqueue(45)
q.enqueue(15)

print('PQueue: ',q.items)
while not q.isEmpty():
    print("Max Priority = ",q.dequeue())