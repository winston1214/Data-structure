# @Author YoungMinKim
# Data Structure - Linked_list
# 연결된 리스트
class Node: # 단순 연결 리스트를 위한 노드 클래스 생성
    def __init__(self,elem,link=None):
        self.data = elem
        self.link = link
class LinkedList:
    def __init__(self):
        self.head = None
    def isEmpty(self): return self.head == None
    def clear(self): self.head = None
    def size(self): 
        node = self.head # 시작노드
        count = 0
        while not node == None: # None이 아닐때 까지 다음 노드로 이동하고
            node = node.link
            count+=1 # 하나씩 count++
        return count
    def display(self,msg = 'LinkedList'):
        print(msg,end=' ')
        node = self.head
        while not node == None:
            print(node.data,end = '->')
            node= node.link # 출력 후 다음으로 넘어가라
        if node == None:
            print('None')
        print()
    def getNode(self,pos): # pos번째 노드 반환
        if pos<0 : return None
        node = self.head # node는 head부터 시작
        while pos>0 and node != None:
            node = node.link # 다음 노드로 이동
            pos -= 1 # pos 하나씩 감소
        return node
    def getEntry(self,pos):# pos번쨰 노드의 데이터 반환
        node = self.getNode(pos)
        if node == None: return None
        else:return node.data
    def replace(self,pos,elem): # pos번째 노드의 데이터 변경
        node = self.getNode(pos)
        if node != None: node.data =elem
    def find(self,data): # 데이터로 data를 같는 노드 반환
        node = self.head
        while node is not None:
            if node.data == data: return node
            node = node.link
        return node
    def insert(self,pos,elem):
        before = self.getNode(pos-1)
        if before == None:
            self.head = Node(elem,self.head)
        else:
            node= Node(elem,before.link)
            before.link = node
    def delete(self,pos):
        before = self.getNode(pos-1)
        if before == None:
            if self.head is not None:
                self.head = self.head.link
        elif before.link != None:
            before.link = before.link.link
s= LinkedList()
s.display('단순 연결 리스트로 구현한 리스트(초기상태): ')
s.insert(0,10);s.insert(0,20);s.insert(1,30);s.insert(s.size(),40);s.insert(2,50)
s.display('단순 연결 리스트로 구현한 리스트(삽입x5): ')
s.replace(2,90)
s.display('단순 연결 리스트로 구현한 리스트(교체):')
s.delete(2);s.delete(s.size()-1);s.delete(0)
s.display('단순 연결 리스트로 구현한 리스트(삭제*3):')
s.clear()
s.display('단순 연결 리스트로 구현한 리스트(정리 후):')