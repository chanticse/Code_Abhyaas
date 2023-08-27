def union(list1, list2):
    union_dict = {}
    
    for element in list1:
        union_dict[element] = True
    
    for element in list2:
        union_dict[element] = True
    
    return list(union_dict.keys())

# Take input from the user for the two lists
ilist1 = input("Enter elements for list1: ")
ilist2 = input("Enter elements for list2: ")

list1 = list(map(int, ilist1.split()))
list2 = list(map(int, ilist2.split()))

union_result = union(list1, list2)
print("Union of the two lists:", union_result)
