# @Author YoungMinKim
# Data structure - Sequential search

def sequential_search(A,key,low,high): # 정렬되지 않아도 괜찮다.
    for i in range(low,high+1): # low~high까지 모두 검사
        if A[i] == key:
            print(i) # return i
    print(None) # return None
data=[9,5,8,3,7]
sequential_search(data,5,0,4)