def subsort(left,right):
    pivot = right
    a =  left - 1 
    
    for k in range(left,right):
        if arr[k] < arr[pivot]:
            a += 1
            arr[a], arr[k] = arr[k], arr[a]
    
    arr[a+1], arr[pivot] = arr[pivot], arr[a+1]
    return a+1
                        
                         
def mainsort(left, right):
    if left <= right:
        p = subsort(left,right)
        mainsort(left,p-1)
        mainsort(p+1,right)
    
    
arr = [4,3,6,1,5,2]
left = 0
right = len(arr) - 1

mainsort(left, right)
print(arr)


# arr = [2,1,3,4,7,5,7,9,6]









# def subsort(i, j, pivot):
    
#     while  i < j:
            
#         while i < len(arr) - 1 and arr[i] < arr[pivot]:
#             i += 1
               
#         while j > 0 and arr[j] > arr[pivot] :
#             j -= 1
            
#         if i < j:
#             arr[i], arr[j] = arr[j], arr[i]
#         else:
#             arr[i], arr[pivot] = arr[pivot], arr[i]
        
#     if i + 1 == pivot or i == pivot:
#         p = -1
            
#     return i
    
# def finalsort(i, j, pivot):
#     p = subsort(i, j, pivot)
    
#     if p == -1:
#         return arr
    
#     subsort(0, i-1, pivot)
#     subsort(i+1, len(arr) - 1, pivot)
#     return arr
        
# #arr = [4,3,6,1,5,2]
# arr = [2,1,3,4,7,5,7,9,6]
# i = 0
# j = len(arr) - 2
# pivot = len(arr) - 1
        
# print(finalsort(i, j, pivot))
    
