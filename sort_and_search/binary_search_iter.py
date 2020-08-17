# @Author YoungMinKim
# Data structure - Binary_search_iteration
def binary_search_iter(A,key,low,high):
    while low<=high:
        middle = (low+high)//2
        if key == A[middle]:
            return middle
        elif key > A[middle]:
            low = middle+1
        else:
            high = middle-1
    return None

data = [5,9,7,8,1]
data.sort()
print(binary_search_iter(data,7,0,len(data)-1))