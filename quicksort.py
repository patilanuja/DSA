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
