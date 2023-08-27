def search(arr, se):
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = left + (right - left) // 2
        
        if arr[mid] == se:
            return mid
        elif arr[mid] < se:
            left = mid + 1
        else:
            right = mid - 1
            
    return -1
arr= input("Enter elements : ")
ilist = list(map(int,arr.split()))

se = int(input("element to search: "))

result = search(ilist,se)

if result != -1:
    print("Element found .")
else:
    print("Element  not found in the array.")
