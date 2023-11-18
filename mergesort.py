
def merge(arr1,arr2):
    new = []
    a = 0 
    b = 0 
    while a < len(arr1) and b < len(arr2):
        if arr1[a] < arr2[b]:
            new.append(arr1[a])
            a += 1
        else:
            new.append(arr2[b])
            b += 1 
                      
    if a < len(arr1):
        new.extend(arr1[a:])
    if b < len(arr2):    
        new.extend(arr2[b:])
            
    return new


def main(arr, left, right):
    if left < right:
        mid = (left + right)//2         
        return merge(main(arr[left:mid+1], 0, len(arr[left:mid+1])-1), main(arr[mid+1:right+1], 0, len(arr[mid+1:right+1])-1))
    return arr    
            
            
arr = [38,27,43,10]
print(main(arr,0,len(arr)-1))