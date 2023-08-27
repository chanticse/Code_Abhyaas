arr=[1,2,3,5,5,6,2,5]
c={}
for i in arr:
    if i in c:
        c[i]+=1
    else:
        c[i]=1
print(c)
max=1
for i in c:
    if c[i]>max:
        max_element=i
        max=c[i]
print(max_element)
min=1
for i in c:
    if c[i]<=min:
        min_element=i
        min=c[i]
print(min_element)
