# @Author YoungMinKim
# Data Structure - Bubble sort
def bubble_sort(A):
    n=len(A)
    for i in range(n-1,0,-1):
        bChanged = False
        for j in range(i):
            if A[j]>A[j+1]: # 순서가 맞지 않으면
                A[j],A[j+1] = A[j+1],A[j] # 교환
                bChanged = True # 교환 발생
        if not bChanged: break
data = [5,3,8,4,9,1,6,2,7]
print('Original: ',data)
bubble_sort(data)
print("Bubble: ",data)