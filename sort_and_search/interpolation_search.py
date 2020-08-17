# @Author YoungMinKim
# Data Structure - interpolation_search

def interpolation_search(A,key,low,high):
    if low<=high:
        middle = int(low+(high-low)*(key-A[low])/(A[high]-A[low])) # key와 현재의 low와 high의 위치 고려
        if key == A[middle]:
            return middle
        elif key < A[middle]:
            return interpolation_search(A,key,low,middle-1)
        else:
            return interpolation_search(A,key,middle+1,high)
data = [3,9,8,1,5]
data.sort()
print(interpolation_search(data,3,0,len(data)-1))