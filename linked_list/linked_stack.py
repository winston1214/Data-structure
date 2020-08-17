# @Author YoungMinKim
# Data structure - Linked Stack

# 단순 연결 리스트 연결 스택 만들기
class Node: # 단순 연결 리스트를 위한 노드 클래스 생성
    def __init__(self,elem,link=None):
        self.data = elem
        self.link = link
class LinkedStack:
    def __init__(self):
        self.top = None # top 생성 및 초기화
    def isEmpty(self):
        return self.top == None
    def clear(self):self.top = None
    def push(self,item): # 삽입 연산
        n=Node(item,self.top) # 입력 데이터를 이용해 노드 생성 후 n 링크가 시작노드를 가르키도록 함
        self.top = n # top이 n을 가리키도록
    def pop(self): # 삭제연산
        if not self.isEmpty():
            n =self.top  # 노드 n이 top을 가르키도록 하고
            self.top = n.link # top이 n의 링크를 가르키도록 한다
            return n.data # 그리고 n이 가르키는 노드를 반환
    def peek(self):
        if not self.isEmpty():
            return self.top.data # 삭제하지 않고 top에 있는 데이터 반환
    def size(self): # 스택의 항목 수 계산
        node = self.top # 시작노드
        count = 0
        while not node == None: # None이 아닐때 까지 다음 노드로 이동하고
            node = node.link
            count+=1 # 하나씩 count++
        return count
    def display(self,msg = 'LinkedStack'):
        print(msg,end=' ')
        node = self.top
        while not node == None:
            print(node.data,end = ' ')
            node= node.link # 출력 후 다음으로 넘어가라
        print()
# test main
odd = LinkedStack()
even = LinkedStack()
for i in range(10):
    if i%2 == 0:even.push(i)
    else: odd.push(i)
even.display('even push 5회')
odd.display('odd push 5회')
for _ in range(2): even.pop()
for _ in range(3): odd.pop()
even.display('even pop 2회')
odd.display('odd pop 2회')