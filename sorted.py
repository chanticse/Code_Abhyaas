def sort(arr):
    ascending = descending = True
    
    for i in range(1, len(arr)):
        if arr[i] < arr[i - 1]:
            ascending = False
        if arr[i] > arr[i - 1]:
            descending = False
            
    return ascending or descending

a= input("Enter elements :")
b= list(map(int,a.split()))

r = sort(b)

if r:
    print("The array is sorted.")
else:
    print("The array is not sorted.")
