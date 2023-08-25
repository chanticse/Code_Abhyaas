def rotate(arr):
    if not arr:
        return arr
    
    le = arr[-1]
    for i in range(len(arr) - 1, 0, -1):
        arr[i] = arr[i - 1]
    arr[0] = le
    
    return arr
a= input("Enter elements :")
b = list(map(int,a.split()))

r= rotate(b)
print(r)

