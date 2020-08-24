# @Author YoungMinKim
# Data Structure - HashChainMap

class Node: 
    def __init__(self,elem,link=None):
        self.data = elem
        self.link = link
class Entry:
    def __init__(self,key,value):
        self.key = key
        self.value = value
    def __str__(self):
        return str('{}{}'.format(self.key,self.value))
class HashChainmap:
    def __init__(self,M):
        self.M = M
        self.table = [None]*M
        
    def hashFn(self,key): # hash func
        sum=0
        for c in key: # 모든 문자열에 대해
            sum+=ord(c) # 아스키 코드 값을 모두 더함
        return sum%self.M
    def insert(self,key,value):
        idx= self.hashFn(key) # hash 주소 계산
        self.table[idx] = Node(Entry(key,value),self.table[idx])
    def search(self,key):
        idx = self.hashFn(key)
        node= self.table[idx]
        while node is not None:
            if node.data.key == key:
                return node.data
            node= node.link
        return node
    def delete(self,key):
        idx = self.hashFn(key)
        node = self.table[idx]
        before= None
        while node is not None:
            if node.data.key == key:
                if before == None:
                    self.table[idx] = node.link
                else:
                    before.link = node.link
                return
            before=node
            node=node
    def display(self,msg):
        print(msg)
        for idx in range(len(self.table)):
            node= self.table[idx]
            if node is not None:
                print("[%2d] ->"%idx,end='')
                while node is not None:
                    print(node.data,end=' -> ')
                    node=node.link
                print()

map = HashChainmap(7)
map.insert('data','자료')
map.insert('structure','구조')
map.insert('sequential search','선형탐색')
map.insert('game','게임')
map.insert('binary search','이진탐색')
map.display("My dictionary: ")
print("search: game ----->",map.search('game'))
print("search: over ----->",map.search('over'))
print("search: data ----->",map.search('data'))
map.delete('game')
map.display("My dictionary: ")