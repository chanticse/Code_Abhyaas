def search(arr, se):
    for i in arr:
        if i == se:
            return i
    return -1
arr = input("Enter elements :")
ilist = list(map(int, arr.split()))

se = int(input("Element to search : "))

result =search(ilist, se)

if result != -1:
    print(f"Element is found ")
else:
    print(f"Element not found in the array.")
