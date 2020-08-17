# @Author YoungMinKim
# Data structure - insertion_sort
def insertion_sort(A):
    n=len(A)
    for i in range(1,n):
        key = A[i]
        j=i-1
        while j>=0 and A[j]>key: # key값 보다 크면
            A[j+1] = A[j] # 항목들 뒤로 이동
            j-=1
        A[j+1] = key # 항목 삽입
data = [5,3,8,4,9,1,6,2,7]
print('Original: ',data)
insertion_sort(data)
print("Insertion: ",data)