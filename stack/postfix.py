# @Author YoungMinKim
# Data structure - Stack
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

def evalPostfix(expr): # 후위표기식 계산
    s=Stack()
    for token in expr:
        if token in "+-*/": # 연산자이면
            val2 = s.pop()
            val1 = s.pop()
            if token == '+': s.push(val1+val2)
            elif token == '-' : s.push(val1-val2)
            elif token == '*': s.push(val1*val2)
            elif token == '/': s.push(val1/val2)
        else:
            s.push(float(token)) # 연산자 아니면 실수형으로 저장
    return s.pop()
expr1 = list('82/3-32*+')
expr2 = list('12/4*14/*')
print('{} --> result : {}'.format(expr1,evalPostfix(expr1)))
print('{} --> result: {}'.format(expr1,evalPostfix(expr2)))