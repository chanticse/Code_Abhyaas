def duplicates(arr):
    ue = []
    se = set()
    
    for e in arr:
        if e not in se:
            ue.append(e)
            se.add(e)
    
    return ue
a = input("Enter elements")
b = list(map(int,a.split()))

r =duplicates(b)
print(r)
