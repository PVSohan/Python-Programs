def binary_search(arr, target):
    left, right = 0, len(arr) - 1 

    while left <= right:
        mid = left + (right - left) // 2  
        
    
        if arr[mid] == target:
            return mid
        
        elif arr[mid] < target:
            left = mid + 1
        
        else:
            right = mid - 1

    return -1  


bk_ID = [1, 2, 3, 4, 5, 6]
bk_p = 5
b_search = binary_search(bk_ID, bk_p)
print("The target position:",b_search)
