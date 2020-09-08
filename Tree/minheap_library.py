# @Author YoungMinKim
# Data structure - Minheap using library
import heapq
arr = [5,3,8,4,9,1,6,2,7]
print(arr)
heapq.heapify(arr) # minheap
print(arr)
print(heapq.heappop(arr)) # delete minimize
print(heapq.heappop(arr)) # delete minimize
print(heapq.heappop(arr)) # delete minimize
print(arr) # after delete minheap