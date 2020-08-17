# @Author YoungMinKim
# Data structure - selection_sort

def selection_sort(A):
    n = len(A)
    for i in range(n-1):
        least = i
        for j in range(i+1,n): 
            if A[j]<A[least]: # least 위치 값보다 j 값이 크면 
                least = j # least를 j로 할당
        A[i],A[least] = A[least],A[i] # 위치 변환

data= [5,3,8,4,9,1,6,2,7]
print("Original: ",data)
selection_sort(data)
print("Selection_sort: ",data)