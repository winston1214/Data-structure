# huffman code 가변 문자열 길이
import heapq
def make_tree(freq):
    heap=[]
    for n in freq:
        heapq.heappush(heap,n)
    for _ in range(n):
        e1=heapq.heappop(heap)
        e2=heapq.heappop(heap)
        heapq.heappush(heap,e1+e2)
        print(e1,e2)
