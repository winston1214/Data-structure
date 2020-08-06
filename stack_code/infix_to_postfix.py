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

def precedence(op): # 우선순위 구현 함수
    if op =='(' or op==')': return 0
    elif op == '+' or op == '-': return 1
    elif op == '*' or op == '/': return 2
    else: return -1

def Infix2Postfix(expr):
    s=Stack()
    output=[]
    for term in expr:
        if term in '(':
            s.push('(')
        elif term in ')':
            while not s.isEmpty(): 
                op = s.pop()
                if op == '(' : break; # 왼쪽괄호가 나올때까지 스택에서 연산자를 꺼내 출력
                else: output.append(op)
        elif term in "+-*/":
            while not s.isEmpty():
                op=s.peek()
                if (precedence(term)<=precedence(op)):
                    output.append(op)
                    s.pop()
                else: break
            s.push(term)
        else:
            output.append(term)
    while not s.isEmpty():
        output.append(s.pop())
    return output
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
expr1 = list('8/2-3+(3*2)')
expr2 = list('1/2*4*(1/4)')
postfix1 = Infix2Postfix(expr1)
postfix2= Infix2Postfix(expr2)
result1 = evalPostfix(postfix1)
result2 = evalPostfix(postfix2)
print("중위표기: ",expr1)
print("후위표기: ",postfix1)
print("결과: ",result1,end='\n\n')
print("중위표기: ",expr2)
print("후위표기: ",postfix2)
print("결과: ",result2,end='\n\n')