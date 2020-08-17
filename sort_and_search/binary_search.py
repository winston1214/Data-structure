# @Author YoungMinKim
# Data structure - binary_search_recursion

# 이진탐색(순환)-> 정렬된 리스트에서 찾기
def binary_search(A,key,low,high):
    if low <= high:
        middle = (low+high) // 2 # 중간값을 기준으로 탐색
        if key == A[middle]:
            return middle
        elif key<A[middle]:
            return binary_search(A,key,low,middle-1)
        else:
            return binary_search(A,key,middle+1,high)
    return None
data = [9,5,8,3,7]
data.sort()
print(binary_search(data,9,0,4))



