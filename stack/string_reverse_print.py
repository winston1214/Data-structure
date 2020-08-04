# @Author YoungMinKim
# Data Structure - Stack
class Stack:
    def __init__(self):
        self.top=[]
    def isEmpty(self):return len(self.top) == 0
    def size(self): return len(self.top)
    def clear(self): self.top=[]
    def push(self,item): # 삽입
        self.top.append(item)
    def pop(self): # 삭제(마지막 부분)
        if not self.isEmpty():
            return self.top.pop(-1)
    def peek(self): # 맨 위의 항목을 반환
        if not self.isEmpty():
            return self.top[-1]

string = str(input('문자열을 입력하시오: '))
s=Stack()

for i in string:
    s.push(i)
while not s.isEmpty():
    print(s.pop(),end='')
