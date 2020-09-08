# @Author YoungMinKim
# Data structure - MaxHeap

class MaxHeap:
    def __init__(self): 
        self.heap = [] # 리스트를 이용한 힙
        self.heap.append(0) # 0번 항목은 사용 X
    def size(self): return len(self.heap)-1 # heap 크기
    def isEmpty(self): return self.size() ==0 # 공백 검사
    def Parent(self,i): return self.heap[i//2] # 부모노드 반환
    def Left(self,i): return self.heap[i*2] # 왼쪽 자식 노드 반환
    def Right(self,i): return self.heap[i*2+1] # 오른쪽 자식 노드 반환
    def display(self,msg='힙 트리: '): print(msg,self.heap[1:])
    def insert(self,n):
        self.heap.append(n) # 맨 마지막 노드로 삽입
        i = self.size() # 노드 n의 위치
        while i != 1 and n>self.Parent(i): # 부모보다 큰 동안 계속 업핍
            self.heap[i] = self.Parent(i) # 부모를 끌어내림
            i=i//2 # i를 부모 인덱스로 올림
        self.heap[i]=n # 마지막 위치에 n 삽입
    def delete(self):
        parent = 1
        child = 2
        if not self.isEmpty():
            hroot = self.heap[1] # 삭제할 루트 복사
            last = self.heap[self.size()] # 마지막 노드
            while child<=self.size(): # 마지막 노드 전까지
                if child<self.size() and self.Left(parent)<self.Right(parent): # 오른쪽 노드가 더 크면 child +1
                    child +=1
                if last >= self.heap[child]: # 마지막 노드보다 더 큰 자식보다 작으면
                    break # 종료
                self.heap[parent] = self.heap[child] # 다운힙 계속
                parent = child
                child *= 2
            self.heap[parent] = last # 맨 마지막 노드를 parent 위치에 복사
            self.heap.pop(-1) # 맨 마지막 노드 삭제
            return hroot # 저장한 루트 반환
heap = MaxHeap()
data = [2,5,4,8,9,3,7,3]
print('Insert: ',data)
for elem in data:
    heap.insert(elem)
heap.display('After Insert: ')
heap.delete()
heap.display('After delete: ')
heap.delete()
heap.display('After delete: ')

