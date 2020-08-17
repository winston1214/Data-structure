# data structure - stack

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
def checkBrackets(statement): # 괄호 검사기
    stack = Stack()
    for ch in statement:
        if ch in ('(','{','['): # 처음 시작 괄호를 스택에 넣는다.
            stack.push(ch)
        elif ch in (')','}',']'):
            if stack.isEmpty(): # 처음 시작 괄호가 스택에 없는데 닫는게 나와버리면 안됨.
                return False
            else:
                left = stack.pop() # 하나씩 뺀다.
                if (ch == ']' and left != '[') or (ch == '}' and left != '{') or (ch == ')' and left != '('):
                    return False # 닫는 괄호인데 하나씩 뺐을 때 짝이 안맞으면 안됨.
    return stack.isEmpty() # 비어야된다. 남아있으면 False 반환

ch=("A[(i+1)]=0","if((i==0) &&(j==0)","A[(i+1])=0")
for c in ch:
    m=checkBrackets(c)
    print('{} 검사 결과는 {}'.format(c,m))