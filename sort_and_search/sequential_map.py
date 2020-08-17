# @Author YoungMinKim
# Data structure - map(Sequential)
class Entry:
    def __init__(self,key,value):
        self.key = key
        self.value = value
    def __str__(self):
        return str('{}{}'.format(self.key,self.value))
class SequentialMap: # 순차탐색 맵
    def __init__(self):
        self.table=[]
    def size(self): return len(self.table)
    def display(self,msg):
        print(msg)
        for entry in self.table:
            print(" ",entry)
    def insert(self,key,value):
        self.table.append(Entry(key,value))
    def search(self,key):
        pos = sequential_search(self.table,key,0,self.size()-1) # 순차탐색
        if pos is not None:
            return self.table[pos]
        else:return None
    def delete(self,key):
        for i in range(self.size()):
            if self.table[i] == key:
                self.table.pop()
                return
def sequential_search(A,key,low,high): # 정렬되지 않아도 괜찮다.
    for i in range(low,high+1): # low~high까지 모두 검사
        if A[i] == key:
            return i
    return None
map = SequentialMap()
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