# @Author YoungMinKim
# Data structure - Using binaryTree

table = [('A','.-'),('B','-...'),('C','-.-.'),('D','-..'),('E','.'),('F','..-.'),('G','--.'),\
    ('H','....'),('I','..'),('J','.---'),('K','-.-'),('L','.-..'),('M','--'),('N','-.'),('O','---'),\
    ('P','.--.'),('Q','--.-'),('R','.-.'),('S','...'),('T','-'),('U','..-'),('V','...-'),('W','.--'),\
        ('X','-..-'),('Y','-.--'),('Z','--..')]
class TNode:
    def __init__(self,data,left,right):
        self.data = data
        self.left = left
        self.right = right
def make_morse_tree():
    root = TNode(None,None,None)
    for tp in table:
        code = tp[1] # 모스부호
        node = root
        for c in code: # 맨 마지막 문자 이전까지 이동
            if c== '.':  # 왼쪽 ㄱ
                if node.left == None: # 비었으면
                    node.left = TNode(None,None,None) # 빈노드 생성
                node = node.left # 안비었으면 그걸로 이동
            elif c == '-':
                if node.right == None:
                    node.right = TNode(None,None,None)
                node = node.right
        node.data = tp[0] # 코드의 알파벳
    return root
def decode(root,code):
    node = root
    for c in code: # 맨 마지막 문자 이전까지 이동
        if c=='.': node= node.left # . 이면 왼쪽
        elif c== '-': node=node.right # - 이면 오른쪽
    return node.data # 문자열 반환
def encode(ch):
    idx = ord(ch) - ord('A') # 리스트에서 해당 문자의 인덱스
    return table[idx][1] # 해당 문자의 모르스 부호 반환

morseCodeTree = make_morse_tree()
string = input('입력 문장: ')
mlist=[]
for ch in string:
    code=encode(ch)
    mlist.append(code)
print('Morse Code: ',mlist)
print('Decoding: ',end='')
for code in mlist:
    ch=decode(morseCodeTree,code)
    print(ch,end='')
print()
